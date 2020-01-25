#
# TODO: default config for PLD - edit /etc/changetrack.conf

%define		src_name	change
%define		src_ver		4_5

Summary:	Changetrack
Name:		changetrack
Version:	4.5
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/changetrack/%{src_name}%{src_ver}.tar.gz
# Source0-md5:	d37ec3c73de430972f7f5729ca3b8e74
Source1:	%{name}-cron
URL:		http://changetrack.sourceforge.net/
BuildRequires:	rpm-perlprov
Requires:	crondaemon
Requires:	perl-modules
Requires:	perl-tools
Requires:	rcs
Requires:	smtpdaemon
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
changetrack is a program to monitor changes to a bunch of files. If
files are modify one day, and the machine start working incorrectly
some days later, changetrack can provide information on which files
were modified, and help locate the problem. Changetrack will also
allow recovery of the files from any stage.

This program makes human-readable output, and also uses RCS to allow
recovery of any stage of revision.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir},/etc/cron.d,%{_var}/lib/%{name}}

install changetrack $RPM_BUILD_ROOT%{_bindir}
install changetrack.man $RPM_BUILD_ROOT%{_mandir}/man1/changetrack.1
install changetrack.conf $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_bindir}/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}
%{_mandir}/man1/changetrack.1*
%dir %{_var}/lib/%{name}
