Summary:	User help for MATE
Summary(pl.UTF-8):	Pomoc użytkownika dla środowiska MATE
Name:		mate-user-guide
Version:	1.26.2
Release:	1
License:	FDL v1.1+
Group:		Documentation
Source0:	https://pub.mate-desktop.org/releases/1.26/%{name}-%{version}.tar.xz
# Source0-md5:	ee8ba05a8760b91adaa8494f2583d8a6
Patch0:		noarch-build.patch
URL:		https://mate-desktop.org/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires:	yelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
User help for MATE.

%description -l pl.UTF-8
Pomoc użytkownika dla środowiska MATE.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
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

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f mate-user-guide.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_desktopdir}/mate-user-guide.desktop
