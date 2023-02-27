workspace(name = "droid-r2bk")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_skylib",
    sha256 = "f24ab666394232f834f74d19e2ff142b0af17466ea0c69a3f4c276ee75f6efce",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.4.0/bazel-skylib-1.4.0.tar.gz",
        "https://github.com/bazelbuild/bazel-skylib/releases/download/1.4.0/bazel-skylib-1.4.0.tar.gz",
    ],
)

http_archive(
    name = "rules_python",
    sha256 = "8c15896f6686beb5c631a4459a3aa8392daccaab805ea899c9d14215074b60ef",
    strip_prefix = "rules_python-0.17.3",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.17.3.tar.gz",
)

http_archive(
    name = "rules_conda",
    sha256 = "ee187c4902f5f8da85fcba9943064fd38b2a75f80ed0a2844b34cf9e27cb5990",
    url = "https://github.com/spietras/rules_conda/releases/download/0.2.0/rules_conda-0.2.0.zip"
)

http_archive(
    name = "rules_proto",
    sha256 = "dc3fb206a2cb3441b485eb1e423165b231235a1ea9b031b4433cf7bc1fa460dd",
    strip_prefix = "rules_proto-5.3.0-21.7",
    urls = [
        "https://github.com/bazelbuild/rules_proto/archive/refs/tags/5.3.0-21.7.tar.gz",
    ],
)

http_archive(
    name = "build_stack_rules_proto",
    sha256 = "ac7e2966a78660e83e1ba84a06db6eda9a7659a841b6a7fd93028cd8757afbfb",
    strip_prefix = "rules_proto-2.0.1",
    urls = ["https://github.com/stackb/rules_proto/archive/v2.0.1.tar.gz"],
)

http_archive(
    name = "io_bazel_rules_go",
    sha256 = "56d8c5a5c91e1af73eca71a6fab2ced959b67c86d12ba37feedb0a2dfea441a6",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.37.0/rules_go-v0.37.0.zip",
        "https://github.com/bazelbuild/rules_go/releases/download/v0.37.0/rules_go-v0.37.0.zip",
    ],
)

http_archive(
    name = "bazel_gazelle",
    sha256 = "ecba0f04f96b4960a5b250c8e8eeec42281035970aa8852dda73098274d14a1d",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-gazelle/releases/download/v0.29.0/bazel-gazelle-v0.29.0.tar.gz",
        "https://github.com/bazelbuild/bazel-gazelle/releases/download/v0.29.0/bazel-gazelle-v0.29.0.tar.gz",
    ],
)

http_archive(
    name = "rules_python_gazelle_plugin",
    sha256 = "",
    strip_prefix = "rules_python-0.17.0/gazelle",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.17.0.tar.gz",
)

## rules_cc defines rules for generating C++ code from Protocol Buffers.
#http_archive(
#    name = "rules_cc",
#    sha256 = "35f2fb4ea0b3e61ad64a369de284e4fbbdcdba71836a5555abb5e194cf119509",
#    strip_prefix = "rules_cc-624b5d59dfb45672d4239422fa1e3de1822ee110",
#    urls = [
#        "https://mirror.bazel.build/github.com/bazelbuild/rules_cc/archive/624b5d59dfb45672d4239422fa1e3de1822ee110.tar.gz",
#        "https://github.com/bazelbuild/rules_cc/archive/624b5d59dfb45672d4239422fa1e3de1822ee110.tar.gz",
#    ],
#)
#
## rules_java defines rules for generating Java code from Protocol Buffers.
#http_archive(
#    name = "rules_java",
#    sha256 = "ccf00372878d141f7d5568cedc4c42ad4811ba367ea3e26bc7c43445bbc52895",
#    strip_prefix = "rules_java-d7bf804c8731edd232cb061cb2a9fe003a85d8ee",
#    urls = [
#        "https://mirror.bazel.build/github.com/bazelbuild/rules_java/archive/d7bf804c8731edd232cb061cb2a9fe003a85d8ee.tar.gz",
#        "https://github.com/bazelbuild/rules_java/archive/d7bf804c8731edd232cb061cb2a9fe003a85d8ee.tar.gz",
#    ],
#)
#
## rules_proto defines abstract rules for building Protocol Buffers.
#http_archive(
#    name = "rules_proto",
#    sha256 = "2490dca4f249b8a9a3ab07bd1ba6eca085aaf8e45a734af92aad0c42d9dc7aaf",
#    strip_prefix = "rules_proto-218ffa7dfa5408492dc86c01ee637614f8695c45",
#    urls = [
#        "https://mirror.bazel.build/github.com/bazelbuild/rules_proto/archive/218ffa7dfa5408492dc86c01ee637614f8695c45.tar.gz",
#        "https://github.com/bazelbuild/rules_proto/archive/218ffa7dfa5408492dc86c01ee637614f8695c45.tar.gz",
#    ],
#)
#
#git_repository(
#    name = "com_google_protobuf",
#    remote = "https://github.com/protocolbuffers/protobuf",
#    shallow_since = "1570061847 -0700",
#    commit = "6d4e7fd7966c989e38024a8ea693db83758944f1",
#)

# Make sure we are using the right bazel version.
load("@bazel_skylib//lib:versions.bzl", "versions")
versions.check("6.0.0")

### Load Go dependencies needed for Gazelle. ###

load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")
load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies", "go_repository")

go_rules_dependencies()
go_register_toolchains(version = "1.19.5")
gazelle_dependencies()

#load("@rules_python_gazelle_plugin//:deps.bzl", _py_gazelle_deps = "gazelle_deps")
#_py_gazelle_deps()

# Load the conda environment and set the toolchain.
load("@rules_conda//:defs.bzl", "conda_create", "load_conda", "register_toolchain")
load_conda(quiet = False)
conda_create(
    name = "conda_env_2022101801",
    environment = "@//:conda_env.yml",
    quiet = False,
)
register_toolchain(env = "conda_env_2022101801")


### Load proptobuf functions and dependencies. ###

register_toolchains("@build_stack_rules_proto//toolchain:standard")

load("@build_stack_rules_proto//deps:core_deps.bzl", "core_deps")
core_deps()

load("@build_stack_rules_proto//:go_deps.bzl", "gazelle_protobuf_extension_go_deps")
gazelle_protobuf_extension_go_deps()

load("@build_stack_rules_proto//deps:protobuf_core_deps.bzl", "protobuf_core_deps")
protobuf_core_deps()

