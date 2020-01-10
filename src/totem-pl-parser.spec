Summary: Playlist Parser Library
Name: totem-pl-parser
Version: 2.28.3
Release: 1
License: LGPL
Group: Libraries/Multimedia
URL: http://www.gnome.org/projects/totem/
Source0: http://ftp.gnome.org/pub/GNOME/sources/totem/2.20/totem-pl-parser-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, pkgconfig, gettext, scrollkeeper
BuildRequires: perl-XML-Parser

%description
Totem-pl-parser is a library for parsing the various playlist formats used for 
online audio and video streams.

%package devel
Summary: Libraries/include files for Totem-pl-parser.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Totem-pl-parser is a library for parsing the various playlist formats used for
online audio and video streams.

This package contains the libraries and includes files necessary to develop
applications with Totem's plparser library.


%prep
%setup -q

%build
%configure 

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# no static libs and libtool archives either
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LIB ChangeLog NEWS README
%{_libdir}/libtotem-plparser.so.*
%{_libdir}/libtotem-plparser-mini.so.*
%{_datadir}/gtk-doc/html
%{_datadir}/locale

%files devel
%defattr(-, root, root)
%{_includedir}/%{name}/1/plparser
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*so

%changelog
* Fri Feb 29 2008 Christian Schaller <christian@collabora.co.uk>
- First spec file for stand alone library
