Summary:	idnkit - internationalized domain name toolkit
Summary(pl):	idnkit - zestaw narzêdzi do umiêdzynarodowionych nazw domen
Name:		idnkit
Version:	1.0
Release:	2
License:	BSD-like
Group:		Libraries
Source0:	http://www.nic.ad.jp/ja/idn/idnkit/download/sources/%{name}-%{version}-src.tar.gz
# Source0-md5:	e8863c21c5049af358bd59c384ff3e5d
URL:		http://www.nic.ad.jp/en/idn/index.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The 'idnkit' is an open source, BSD-like licensed software that
provides functionalities about Internationalized Domain Name
processing standardized at IETF. Major features that idnkit provides
are as follows:
 - libidnkit - Core library for IDN processing,
 - libidnkitlite - Light Weight library for IDN processing (UTF-8
   only),
 - idnconv - DNS zone / configuration file encoding converter
 - runidn / idn wrapper - Dynamic link resolver library for UNIX /
   Windows

%description -l pl
idnkit to wolnodostêpne na licencji typu BSD oprogramowanie
zapewniaj±ce funkcjonalno¶æ zwi±zan± z obs³ug± umiêdzynarodowionych
nazw domen (IDN - Internationalized Domain Name) standaryzowan± przez
IETF. G³ówne w³asno¶ci dostarczane przez idnkit s± nastêpuj±ce:
 - libidnkit - g³ówna biblioteka do przetwarzania IDN,
 - libidnkitlite - lekka biblioteka do przetwarzania IDN (tylko UTF-8),
 - idnconv - konwerter kodowania plików konfiguracyjnych i stref DNS
 - runidn / idn wrapper - dynamicznie linkowana biblioteka resolvera
   dla uniksów i Windows.

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
%config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/idn.conf
%config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/idnalias.conf
%attr(755,root,root) %{_bindir}/idnconv
%attr(755,root,root) %{_bindir}/runidn
%attr(755,root,root) %{_libdir}/libidnkit*.so.*.*.*
# this one is used by runidn
%{_libdir}/libidnkitres.la
%dir %{_datadir}/idnkit
%{_datadir}/idnkit/*.map
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libidnkit*.so
%{_libdir}/libidnkit.la
%{_libdir}/libidnkitlite.la
%dir %{_includedir}/idn
%{_includedir}/idn/*.h
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libidnkit*.a
