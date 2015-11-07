Summary:	User help for MATE
Summary(pl.UTF-8):	Pomoc użytkownika dla środowiska MATE
Name:		mate-user-guide
Version:	1.12.0
Release:	1
License:	CC-BY-SA v3.0
Group:		Documentation
Source0:	http://pub.mate-desktop.org/releases/1.12/%{name}-%{version}.tar.xz
# Source0-md5:	a530d4e10e7ea5a670467aa8f545b13b
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

%find_lang mate-user-guide --with-mate

%clean
rm -rf $RPM_BUILD_ROOT

%files -f mate-user-guide.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_desktopdir}/mate-user-guide.desktop
