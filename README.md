# Dependency Review Configuration

This repository contains a configuration file for GitHub's [Dependency Review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review) action. It defines the set of **allowed licenses** for open source dependencies used across projects in our organization.

## Purpose

The goal of this repository is to centralize and standardize license policies. By explicitly listing allowed licenses, we ensure consistent license compliance and reduce legal risk when integrating third-party software.

## Configuration File

- **Path**: `.github/dependency-review.yml`
- **Type**: GitHub Advanced Security policy configuration
- **Purpose**: Defines a whitelist of open source licenses that are permitted in the projects using this config.

## Example Usage

To use this configuration in your own repository, add the following to your GitHub Actions workflow:

```yaml
- uses: actions/dependency-review-action@v4
  with:
    config-file: https://raw.githubusercontent.com/hpi-schul-cloud/dependency-review-config/main/dependency-review.yml
```

License Policy

The configuration explicitly lists licenses that have been reviewed and approved. Typical examples include:
- MIT
- Apache-2.0
- BSD-2-Clause
- BSD-3-Clause
- ISC

For the complete list, see the contents of the dependency-review.yml file.