Summary:	User help for MATE
Summary(pl.UTF-8):	Pomoc użytkownika dla środowiska MATE
Name:		mate-user-guide
Version:	1.14.0
Release:	2
License:	FDL v1.1+
Group:		Documentation
Source0:	http://pub.mate-desktop.org/releases/1.14/%{name}-%{version}.tar.xz
# Source0-md5:	553a172785de8255ff547287a091b29b
URL:		http://mate-desktop.org/
BuildRequires:	gettext-tools
BuildRequires:	intltool >= 0.40.0
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

# es_419,zh-Hans are bogus; frp,jv,ku_IQ,nah,nqo,sco not supported by glibc; ur_PK an empty copy of ur
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{es_419,frp,jv,ku_IQ,nah,nqo,sco,ur_PK,zh-Hans}

%find_lang mate-user-guide --with-mate

%clean
rm -rf $RPM_BUILD_ROOT

%files -f mate-user-guide.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_desktopdir}/mate-user-guide.desktop
