Summary:	User help for MATE
Summary(pl.UTF-8):	Pomoc użytkownika dla środowiska MATE
Name:		mate-user-guide
Version:	1.24.0
Release:	1
License:	FDL v1.1+
Group:		Documentation
Source0:	http://pub.mate-desktop.org/releases/1.24/%{name}-%{version}.tar.xz
# Source0-md5:	28ccf87374000cb8d4015bdc7e4df4ad
URL:		http://mate-desktop.org/
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	yelp-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
User help for MATE.

%description -l pl.UTF-8
Pomoc użytkownika dla środowiska MATE.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# frp,jv,ku_IQ,pms not supported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{es_ES,frp,ie,jv,ku_IQ,pms}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/help/{ie,ku_IQ}

%find_lang mate-user-guide --with-mate

%clean
rm -rf $RPM_BUILD_ROOT

%files -f mate-user-guide.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_desktopdir}/mate-user-guide.desktop
