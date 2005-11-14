%define		_splash		keramik

Summary:	keramik splash screen
Summary(pl):	Ekran startowy keramik
Name:		kde-splash-%{_splash}
Version:	1
Release:	5
License:	GPL
Group:		Themes
#Source0:	http://www.kde-look.org/content/download.php?content=1983
Source0:	%{version}983-keramik_splash.tgz
# Source0-md5:	bb9d9ca1e685f61038a7fd4e27d4ec00
Source1:	%{name}-Preview.png
Source2:	%{name}-Theme.rc
URL:		http://www.kde-look.org/content/show.php?content=1983
Requires:	kdebase-desktop >= 9:3.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A transparent splash screen with keramik window decoration around it,
crystal icons and a picture consisting of KDE Logo and a flat monitor
drawing.

%description -l pl
Przezroczysty ekran startowy z ikonami z motywu crystal oraz dekoracja
okna keramik dooko³a g³ównego obrazka, który sk³ada siê z logo KDE i
rysunku monitora ciek³okrystalicznego.

%prep
%setup -q -n %{_splash}_splash

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

cp *.* $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

install %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}/Preview.png

install %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}/Theme.rc


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/%{_splash}
