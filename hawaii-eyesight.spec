Summary:	Hawaii desktop image viewer
Name:		hawaii-eyesight
Version:	0.1.2
Release:	3
Group:		Graphical desktop/Other
License:        GPLv2+
URL:		http://www.maui-project.org
Source0:	http://sourceforge.net/projects/mauios/files/hawaii/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	qt5-devel
BuildRequires:	cmake
BuildRequires:	bzip2-devel

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
