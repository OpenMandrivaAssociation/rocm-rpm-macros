# ROCm RPM macros — version lock and shared build settings for the stack.
# Noarch; does not need LLVM. Land this before any other ROCm rebuild.

%define debug_package %{nil}

Name:		rocm-rpm-macros
Version:	7.14.0
Release:	1
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
