Name:		nginx-ldap-auth
Version:	0.0.3
Release:	2%{?dist}
Summary:	NGINX Plus LDAP authentication daemon

Group:		System Environment/Daemons
License:	2-clause BSD-like license
URL:		https://github.com/nginxinc/nginx-ldap-auth
Source0:	nginx-ldap-auth-release-%{version}.tar.gz

%{?systemd_requires}
BuildRequires:	systemd
Requires:	    systemd

BuildRequires:  python-ldap
Requires:	    python-ldap

BuildRequires:  python-argparse
Requires:	    python-argparse

Requires:	    logrotate
Requires:       nginx

%description
Reference implementation of method for authenticating users on behalf of
servers proxied by NGINX or NGINX Plus.

%prep
%setup -q

%install
ls
install -m 0755 -d %{buildroot}/var/run/%{name}
install -D -m 0755 src/*.py %{buildroot}/var/run/%{name}
install -D -m 0755 scripts/*.sh %{buildroot}/var/run/%{name}
install -m 0755 -d %{buildroot}/var/www/%{name}

cp -R html/* %{buildroot}/var/www/%{name}

install -D -p -m 0644 files/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -D -p -m 0644 files/backend-sample-app.service %{buildroot}%{_unitdir}/backend-sample-app.service
install -D -p -m 0644 files/%{name}.conf %{buildroot}%{_sysconfdir}/nginx/conf.d/%{name}.conf
install -D -p -m 0644 files/%{name}.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

install -m 0755 -d %{buildroot}/var/log/%{name}

%files
%doc README.md LICENSE
%attr(0755, nginx, nginx)   /var/run/%{name}
%attr(0755, nginx, nginx)   /var/run/%{name}/*
%attr(0755, nginx, nginx)   /var/www/%{name}
%attr(0755, nginx, nginx)   /var/www/%{name}/*
%attr(0755, nginx, nginx)   /var/log/%{name}

%{_sysconfdir}/nginx/conf.d/%{name}.conf
%{_sysconfdir}/logrotate.d/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/backend-sample-app.service

%post
/usr/bin/systemctl preset %{name}.service
/usr/bin/systemctl preset backend-sample-app.service

%preun
/usr/bin/systemctl --no-reload disable %{name}.service >/dev/null 2>&1 ||:
/usr/bin/systemctl stop %{name}.service >/dev/null 2>&1 ||:

/usr/bin/systemctl --no-reload disable backend-sample-app.service >/dev/null 2>&1 ||:
/usr/bin/systemctl stop backend-sample-app.service >/dev/null 2>&1 ||:

%postun
/usr/bin/systemctl daemon-reload >/dev/null 2>&1 ||:

%clean
# rm -rf %{buildroot}

%changelog
* Wed Apr 4 2018 Paulo Mariano <paulomariano77@gmail.com> 0.0.3-2
- Insert a new login page

* Wed Nov 02 2016 Konstantin Pavlov <thresh@nginx.com> 0.0.3-1
- Initial release