%define		_splash		keramik

Summary:	keramik splash screen
Summary(pl):	Ekran startowy keramik
Name:		kde-splash-%{_splash}
Version:	1
Release:	1
License:	GPL
Group:		Themes/Gtk
#Source0:	http://www.kde-look.org/content/download.php?content=1983
Source0:	1983-keramik_splash.tgz
URL:		http://www.kde-look.org/content/show.php?content=1983
Provides:	kde-splash
Requires:	kdebase >= 3.0.2-7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man
%define         _htmldir        /usr/share/doc/kde/HTML

%description
Keramik splash screen.

%description -l pl
Ekran startowy keramik.

%prep
%setup  -q -n %{_splash}_splash

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d "$RPM_BUILD_ROOT/%{_datadir}/apps/ksplash/pics"
install * "$RPM_BUILD_ROOT/%{_datadir}/apps/ksplash/pics"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/pics/*
