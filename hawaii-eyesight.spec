Summary:	Hawaii desktop image viewer
Name:		eyesight
Version:	0.1.4
Release:	2
Group:		Graphical desktop/Other
License:        GPLv2+
URL:		http://www.hawaiios.org
Source0:	https://github.com/hawaii-desktop/eyesight/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake

%description
Image viewer for the Hawaii desktop.

%prep
%setup -q

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

%find_lang %{name} --all-name --with-qt

%files -f %{name}.lang
%doc COPYING README.md
%dir %{_datadir}/eyesight
%dir %{_datadir}/eyesight/translations
%{_bindir}/eyesight
%{_datadir}/applications/eyesight.desktop
%{_datadir}/eyesight/translations/??.qm
