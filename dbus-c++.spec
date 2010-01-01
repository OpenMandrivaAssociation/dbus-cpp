%define git_date 20090203
%define git_version 13281b3
%define api 1
%define major 0
%define libname %mklibname %name %api %major
%define develname %mklibname -d %name
Name:		dbus-c++
Version:	0.5.0
Release:	%mkrel -c %{git_date} 2
Summary:	Native C++ bindings for D-Bus

Group:		System/Libraries
License:	LGPLv2+
URL:		http://freedesktop.org/wiki/Software/dbus-c++
# Generate tarball
# git clone git://anongit.freedesktop.org/git/dbus/dbus-c++/
# git-archive --format=tar --prefix=dbus-c++/ %{git_version} | bzip2 > dbus-c++-0.5.0.`date +%Y%m%d`git%{git_version}.tar.bz2
Source0:	%{name}-%{version}.%{git_date}git%{git_version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-

Patch1:	dbus-c++-get-uid-api.patch
Patch2: gcc-44.patch
Patch3: dbus-c++-build-fix.patch
Patch4: dbus-c++-fix-linking.patch

BuildRequires:	dbus-devel
BuildRequires:	glib2-devel
Buildrequires:	gtkmm2.4-devel
Buildrequires:	libtool
BuildRequires:	expat-devel

%description
Native C++ bindings for D-Bus for use in C++ programs.

%package -n %libname
Group:		System/Libraries
Summary:	Native C++ bindings for D-Bus

%description -n %libname
Native C++ bindings for D-Bus for use in C++ programs.

%package	-n %develname
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%name >= %version-%release
Provides:	%name-devel = %{version}-%{release}

%description	-n %develname
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}
%{__sed} -i 's/\r//' AUTHORS
%{__sed} -i 's/-O3//' configure.ac
%patch1 -p1 -b .uid
%patch2 -p1 -b .gcc44
%patch3 -p1 -b .buildfix
%patch4 -p1
./autogen.sh

%build
export CPPFLAGS='%{optflags}'
%configure2_5x --disable-static --enable-glib
%make


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_bindir}/dbusxx-introspect
%{_bindir}/dbusxx-xml2cpp

%files -n %libname
%defattr(-,root,root,-)
%{_libdir}/libdbus-c++-%{api}.so.%{major}*

%files -n %develname
%defattr(-,root,root,-)
%doc TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*

