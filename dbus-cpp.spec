%define major 5
%define libname %mklibname dbus-cpp %{major}
%define devname %mklibname dbus-cpp -d

Name: dbus-cpp
Version: 5.0.0
Release: 1
Source0: %{name}-%{version}.tar.xz
Patch0: dbus-cpp-symbol-visibility.patch
Patch1: dbus-cpp-no-broken-tests.patch
Patch2: dbus-cpp-static-cppc-helper.patch
Summary: C++11 bindings to D-Bus
URL: http://code.launchpad.net/dbus-cpp
License: LGPLv3
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: pkgconfig(dbus-1)
BuildRequires: boost-devel
BuildRequires: gmock-source
BuildRequires: pkgconfig(properties-cpp)
BuildRequires: pkgconfig(process-cpp)

%description
A header-only dbus-binding leveraging C++-11

%package -n %{libname}
Summary: C++11 bindings to D-Bus
Group: System/Libraries

%description -n %{libname}
C++11 bindings to D-Bus

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package examples
Summary: Examples for dbus-cpp
Group: Development/C
Requires: %{libname} = %{EVRD}

%prep
%setup -qn %{name}
%autopatch -p1
%cmake -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_bindir}/*
%{_datadir}/dbus-cpp

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files examples
%{_libexecdir}/examples
