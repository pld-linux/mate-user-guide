Summary:	User help for MATE
Summary(pl.UTF-8):	Pomoc użytkownika dla środowiska MATE
Name:		mate-user-guide
Version:	1.10.1
Release:	1
License:	CC-BY-SA v3.0
Group:		Documentation
Source0:	http://pub.mate-desktop.org/releases/1.10/%{name}-%{version}.tar.xz
# Source0-md5:	86fc044062f78d2ea4efdf52573a6749
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

%find_lang mate-help --with-mate

%clean
rm -rf $RPM_BUILD_ROOT

%files -f mate-help.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
#%{_desktopdir}/mate-user-guide.desktop
