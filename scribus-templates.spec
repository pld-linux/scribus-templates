Summary:	Scribus sample templates
Summary(pl.UTF-8):	Przykładowe szablony dla Scribusa
Name:		scribus-templates
Version:	1.2.1
Release:	2
License:	GPL v2
Group:		X11/Applications/Publishing
Source0:	http://www.scribus.org.uk/downloads/%{version}/scribus-temp-all-%{version}.tar.bz2
# Source0-md5:	19d102ff16c295e29bb7a051c66c2c58
URL:		http://www.scribus.net/
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	scribus >= 1.2.1
Requires:	scribus-templates-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains sample templates for Scribus, such as brochures,
calendars and advertisements.

%description -l pl.UTF-8
Pakiet zawiera przykładowe szablony dla Scribusa, takie jak
broszury, kalendarze i ogłoszenia.

%prep
%setup -q

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%dir %{_datadir}/scribus/templates/prog1
%{_datadir}/scribus/templates/prog1/*
