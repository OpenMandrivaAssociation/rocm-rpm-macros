# ROCm RPM macros — version lock and shared build settings for the stack.
# Noarch; does not need LLVM. Land this before any other ROCm rebuild.

%define debug_package %{nil}

Name:		rocm-rpm-macros
Version:	7.14.0
Release:	2
Summary:	RPM macros for building ROCm packages
License:	MIT
Group:		Development/Other
URL:		https://github.com/OpenMandrivaAssociation/rocm-rpm-macros
Source0:	macros.rocm
BuildArch:	noarch

%description
Shared RPM macros for OpenMandriva ROCm packaging: version lock (currently
TheRock 7.14), source URL helpers, FHS install layout, GPU ISA lists, and
common CMake flags.

%%rocm_detect_gpu_archs / %%rocm_detect_gpu_targets intersect clang's
amdgcn CPUs with rocm-device-libs bitcode so a newer ROCm that adds
e.g. gfx1500 is picked up on the next package rebuild. Invoke them
from a spec; the default %%rocm_gpu_targets list stays static so
ordinary rpm queries do not spawn clang.

All ROCm packages should BuildRequires: %{name} and use the macros
rocm_version, rocm_gpu_targets, rocm_cmake_fhs, and friends.

This package ships only text macros — no binaries.

%prep
# nothing to unpack

%build
# nothing to build

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.rocm

%files
%{_rpmmacrodir}/macros.rocm
