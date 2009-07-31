Name:           ocaml-ocamldap
Version:        2.1.8
Release:        %mkrel 1
Summary:        LDAP bindings for OCaml 
License:        LGPL
Group:          Development/Other
URL:            http://homepage.mac.com/letaris/
Source0:        http://homepage.mac.com/letaris/ocamldap-2.1.8.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlnet-devel
BuildRequires:  ocaml-ssl-devel

%description
Ocamldap is an ldap toolkit.  It can be used by ocaml programs to
communicate with ldap servers, and to build your own ldap servers.

Ocamldap supports the core ldap-client functions, including search, add,
modify, and delete.  

Object oriented interface with additional features.
Such as, nice data structures for local ldap entries which
record local modifications and can sync them with the server, fewer
arguments needed to perform simple tasks, and transparent reconnection
of dropped connections.

Ocamldap includes an ldif parser, which allows you to read ldif files into
entry objects. It also supports ldif change records.

Ocamldap has a method call to grab the schema of an ldapv3 server

Basic ldap server functionality (ldap_funserver) allows you to easily
construct your own ldap servers. Perfect for meta directories, 
and other cool projects. Someday maybe your main database :-)

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocamldap-%{version}

%build
make all opt
make documentation
sed -i -e 's/2.1.5/2.1.8/' META

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/ocamldap
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING Changelog README
%dir %{_libdir}/ocaml/ocamldap
%{_libdir}/ocaml/ocamldap/META
%{_libdir}/ocaml/ocamldap/*.cma
%{_libdir}/ocaml/ocamldap/*.cmi
%{_libdir}/ocaml/ocamldap/*.cmo

%files devel
%defattr(-,root,root)
%doc doc/ocamldap
%{_libdir}/ocaml/ocamldap/*.a
%{_libdir}/ocaml/ocamldap/*.o
%{_libdir}/ocaml/ocamldap/*.cmxa
%{_libdir}/ocaml/ocamldap/*.cmx
%{_libdir}/ocaml/ocamldap/*.mli

