%define git_date %{nil}
%define git_version %{nil}
%define api 1
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname -d %name

Name:		dbus-c++
Version:	0.9.0
%if 0%{git_date}
Release:	%mkrel -c %{git_date} 4
%else
Release:	2
%endif

Summary:	Native C++ bindings for D-Bus
Group:		System/Libraries
License:	LGPLv2+
URL:		http://freedesktop.org/wiki/Software/dbus-c++
# Generate tarball
# git clone git://anongit.freedesktop.org/git/dbus/dbus-c++/
# git-archive --format=tar --prefix=dbus-c++/ %{git_version} | bzip2 > dbus-c++-0.5.0.`date +%Y%m%d`git%{git_version}.tar.bz2
%if 0%{git_version}
Source0:	%{name}-%{version}.%{git_date}git%{git_version}.tar.bz2
%else
Source0:	http://downloads.sourceforge.net/project/dbus-cplusplus/%{name}/%{version}/lib%{name}-%{version}.tar.gz
%endif

Patch0:		libdbus-c++-0.9.0-mdv-build_order.patch
Patch1:		libdbus-c++-0.9.0-mdv-linking.patch
Patch2:		dbus-c++-0.9.0-gcc-4.7.patch

BuildRequires:	dbus-devel
BuildRequires:	glib2-devel
BuildRequires:	gtkmm2.4-devel
BuildRequires:	libtool
BuildRequires:	expat-devel
BuildRequires:	ecore-devel

%description
Native C++ bindings for D-Bus for use in C++ programs.

%package -n %{libname}
Group:		System/Libraries
Summary:	Native C++ bindings for D-Bus

%description -n %{libname}
Native C++ bindings for D-Bus for use in C++ programs.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n lib%{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoreconf
%configure2_5x \
		--disable-static \
        --enable-glib \
        --disable-tests

%make

%install
%makeinstall_std

%files
%doc COPYING AUTHORS
%{_bindir}/dbusxx-introspect
%{_bindir}/dbusxx-xml2cpp

%files -n %libname
%{_libdir}/libdbus-c++*-%{api}.so.%{major}*

%files -n %develname
%doc TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
