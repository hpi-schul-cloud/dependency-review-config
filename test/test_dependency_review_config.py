import sys
import yaml

def is_sorted(lst):
    return lst == sorted(lst, key=lambda s: s.lower())

def show_sorting_issues(lst, path):
    expected = sorted(lst, key=lambda s: s.lower())
    print(f"\n❌ List at '{path}' is not sorted alphabetically.")
    print("Current order:")
    for item in lst:
        print(f"  - {item}")
    print("Expected order:")
    for item in expected:
        print(f"  - {item}")
    print()

def check_yaml_sorted_lists(file_path):
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)

    issues_found = False

    def recurse_check(node, path=''):
        nonlocal issues_found
        if isinstance(node, list):
            if not is_sorted(node):
                show_sorting_issues(node, path)
                issues_found = True
        elif isinstance(node, dict):
            for k, v in node.items():
                recurse_check(v, f"{path}.{k}" if path else k)

    recurse_check(data)

    if issues_found:
        print("❌ Sorting issues detected.")
        sys.exit(1)
    else:
        print("✅ YAML lists are sorted correctly.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test_dependency_review_config.py path/to/dependency-review.yml")
        sys.exit(1)

    check_yaml_sorted_lists(sys.argv[1])