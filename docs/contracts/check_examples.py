#!/usr/bin/env python3
"""Validate docs/contracts examples against the DepthSift Companion protocol schemas.

Usage: python3 docs/contracts/check_examples.py
Requires the ``jsonschema`` package (>= 4.18) and its ``referencing`` dependency.
Every file in examples/valid must validate against the envelope schema; every file in
examples/invalid must be rejected, either by JSON Schema or by the duplicate-key check that
specification section 9.5 requires outside JSON Schema. Semantic checks (sessions, sequence,
journal identity, evidence truth) are out of scope here.
"""
import json
import pathlib
import sys

try:
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource
except ImportError:  # pragma: no cover
    print("missing dependency: pip install jsonschema", file=sys.stderr)
    sys.exit(2)

HERE = pathlib.Path(__file__).resolve().parent
ENVELOPE_ID = "urn:depthsift:companion:envelope:1"


class DuplicateKeyError(ValueError):
    pass


def reject_duplicates(pairs):
    seen = set()
    for key, _ in pairs:
        if key in seen:
            raise DuplicateKeyError(f"duplicate JSON key: {key}")
        seen.add(key)
    return dict(pairs)


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh, object_pairs_hook=reject_duplicates)


def build_validator():
    registry = Registry()
    schemas = {}
    for path in sorted(HERE.glob("*.schema.json")):
        schema = load_json(path)
        Draft202012Validator.check_schema(schema)
        schemas[path.name] = schema
        registry = registry.with_resource(schema["$id"], Resource.from_contents(schema))
    envelope = next(s for s in schemas.values() if s["$id"] == ENVELOPE_ID)
    validator = Draft202012Validator(
        envelope, registry=registry, format_checker=Draft202012Validator.FORMAT_CHECKER
    )
    return validator, schemas


def main():
    validator, schemas = build_validator()
    print(f"schemas: {len(schemas)} loaded and self-checked")
    failures = 0
    for path in sorted((HERE / "examples" / "valid").glob("*.json")):
        try:
            errors = sorted(validator.iter_errors(load_json(path)), key=lambda e: list(e.path))
        except DuplicateKeyError as exc:
            errors = [exc]
        status = "ok" if not errors else "FAIL"
        failures += bool(errors)
        print(f"valid/{path.name}: {status}")
        for err in errors[:3]:
            msg = getattr(err, "message", str(err))
            print(f"    {msg[:160]}")
    for path in sorted((HERE / "examples" / "invalid").glob("*.json")):
        try:
            doc = load_json(path)
        except DuplicateKeyError as exc:
            print(f"invalid/{path.name}: rejected (duplicate key)")
            continue
        errors = list(validator.iter_errors(doc))
        status = "rejected" if errors else "FAIL: accepted"
        failures += not errors
        print(f"invalid/{path.name}: {status}")
    print("result:", "all examples behave as expected" if not failures else f"{failures} problem(s)")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
