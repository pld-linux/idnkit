Summary:	idnkit
Name:		idnkit
Version:	1.0
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://www.nic.ad.jp/ja/idn/idnkit/download/sources/%{name}-%{version}-src.tar.gz
# Source0-md5:	e8863c21c5049af358bd59c384ff3e5d
URL:		http://www.nic.ad.jp/en/idn/index.html
BuildRequires:	autoconf
BuildRequires:	libtool
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The 'idnkit' is an open source, BSD-like licensed software that
provides functionalities about Internationalized Domain Name
processing standardized at IETF. Major features that idnkit provides
are as follows.

 - libidnkit - Core library for IDN processing,
 - libidnkitlite - Light Weight library for IDN processing (UTF-8
   only),
 - idnconv - DNS zone / configuration file encoding converter
 - runidn / idn wrapper - Dynamic link resolver library for UNIX /
   Windows

%package devel
Summary:	Header files for idnkit
Summary(pl):	Pliki nag³ówkowe idnkit
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for idnkit.

%description devel -l pl
Pliki nag³ówkowe idnkit.

%package static
Summary:	Static idnkit library
Summary(pl):	Statyczna biblioteka idnkit
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static idnkit library.

%description static -l pl
Statyczna biblioteka idnkit.

%prep
%setup -q -n %{name}-%{version}-src

%build
#%%{__libtoolize}
#%%{__autoconf}
#%%{__aclocal}
%configure2_13 \
	--enable-extra-ace \
	--enable-runidn

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README NEWS
%doc %lang(ja) README.ja
%attr(644,root,root) %config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/idn.conf
%attr(644,root,root) %config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/idnalias.conf
%attr(755,root,root) %{_bindir}/idnconv
%attr(755,root,root) %{_bindir}/runidn
%attr(755,root,root) %{_libdir}/libidnkit*.so.*.*.*
# Yes, this is for dlopen()
%attr(644,root,root) %{_libdir}/libidnkit*.la
%attr(755,root,root) %dir %{_datadir}/idnkit
%attr(644,root,root) %{_datadir}/idnkit/*.map
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libidnkit*.so
%{_includedir}/idn/*.h
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libidnkit*.a
