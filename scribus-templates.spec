Summary:	Scribus sample templates
Summary(pl):	Przyk³adowe szablony dla Scribusa
Name:		scribus-templates
Version:	1.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Publishing
Source0:	http://www.scribus.org.uk/downloads/1.2/scribus-temp-all-%{version}.tar.bz2
# Source0-md5:	f93b4a8dfab66c58654deacc5c86fbeb
URL:		http://www.scribus.net/
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	scribus >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains sample templates for Scribus, such as brochures,
calendars and advertisements.

%description -l pl
Pakiet zawiera przyk³adowe szablony dla Scribusa, takie jak
broszury, kalendarze i og³oszenia.

%prep
%setup -q -n scribus-temp-all-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--prefix=$RPM_BUILD_ROOT/%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%dir %{_datadir}/scribus/templates/ad1
%{_datadir}/scribus/templates/ad1/*
%dir %{_datadir}/scribus/templates/ad2
%{_datadir}/scribus/templates/ad2/*
%dir %{_datadir}/scribus/templates/ad3
%{_datadir}/scribus/templates/ad3/*
%dir %{_datadir}/scribus/templates/ad5
%{_datadir}/scribus/templates/ad5/*
%dir %{_datadir}/scribus/templates/br1
%{_datadir}/scribus/templates/br1/*
%dir %{_datadir}/scribus/templates/br2
%{_datadir}/scribus/templates/br2/*
%dir %{_datadir}/scribus/templates/cal1
%{_datadir}/scribus/templates/cal1/*
%dir %{_datadir}/scribus/templates/cal2
%{_datadir}/scribus/templates/cal2/*
%dir %{_datadir}/scribus/templates/menu1-bw
%{_datadir}/scribus/templates/menu1-bw/*
%dir %{_datadir}/scribus/templates/menu1
%{_datadir}/scribus/templates/menu1/*
%dir %{_datadir}/scribus/templates/menu2
%{_datadir}/scribus/templates/menu2/*
%dir %{_datadir}/scribus/templates/nl1-bw
%{_datadir}/scribus/templates/nl1-bw/*
%dir %{_datadir}/scribus/templates/nl1
%{_datadir}/scribus/templates/nl1/*
%dir %{_datadir}/scribus/templates/nl2
%{_datadir}/scribus/templates/nl2/*
%dir %{_datadir}/scribus/templates/presentation
%{_datadir}/scribus/templates/presentation/*
%dir %{_datadir}/scribus/templates/prog1
%{_datadir}/scribus/templates/prog1/*
%dir %{_datadir}/scribus/templates/textbased
%{_datadir}/scribus/templates/textbased/*
