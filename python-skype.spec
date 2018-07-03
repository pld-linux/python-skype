%define 	module	skype
Summary:	Python wrapper for the Skype API
Name:		python-%{module}
Version:	1.0.32.1
Release:	6
License:	BSD
Group:		Development/Languages/Python
#Source0:	http://downloads.sourceforge.net/skype4py/Skype4Py-%{version}.tar.gz
Source0:	https://github.com/glensc/skype4py/tarball/master/Skype4Py-%{version}.tar.gz
# Source0-md5:	a31d4e99cd184ce916345f422d73b310
Source1:	%{name}-chat.py
Source2:	skype.protocol
Source3:	skype.py
Source4:	skype.schemas
# http://skype4py.svn.sourceforge.net/viewvc/skype4py/Skype4Py/api/posix.py?view=patch&r1=277&r2=276&pathrev=277
Patch0:		default-transport.patch
Patch1:		execlp-args.patch
URL:		http://sourceforge.net/projects/skype4py/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules >= 1:2.5
Requires:	skype-program
Suggests:	python-dbus
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		kde_servicesdir	%{_datadir}/services

%description
Skype4Py is a Python wrapper for the Skype API. It is platform
independant, written completly in Python and reimplements the
Skype4COM's API in a Pythonic way.

%package -n kde-protocol-skype
Summary:	KDE3/KDE4 protocol handler
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description -n kde-protocol-skype
KDE3/KDE4 "skype:" protocol handler.

%package -n gnome-urlhandler-skype
Summary:	Gnome URL handler for "skype:" protocol
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description -n gnome-urlhandler-skype
Gnome URL handler for "skype:" protocol.

%prep
%setup -q -n Skype4Py-%{version} -c
mv *-skype4py-*/* .

%patch0 -p0 -R
%patch1 -p1
%undos -f py

mv Skype4Py/LICENSE .

cp -p %{SOURCE1} examples/chat.py

# wrap each language import so any language becames optional
for lang in $(awk '/^import/{print $2}' Skype4Py/lang/__init__.py | sort -u); do
	 printf "try:\n import $lang\nexcept ImportError:\n pass\n";
done > lang.py
cp -p lang.py Skype4Py/lang/__init__.py

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

# demo
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# kde
install -d $RPM_BUILD_ROOT{%{kde_servicesdir},%{_datadir}/skype}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{kde_servicesdir}
install -p %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/skype

# gnome
install -d $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas
cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas

# ???
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/Skype4Py/lang/x1.py[co]

%clean
rm -rf $RPM_BUILD_ROOT

%post -n gnome-urlhandler-skype
%gconf_schema_install skype.schemas

%preun -n gnome-urlhandler-skype
%gconf_schema_uninstall skype.schemas

%files
%defattr(644,root,root,755)
%doc README LICENSE ChangeLog
%dir %{py_sitescriptdir}/Skype4Py
%{py_sitescriptdir}/Skype4Py/*.py[co]
%dir %{py_sitescriptdir}/Skype4Py/api
%{py_sitescriptdir}/Skype4Py/api/*.py[co]
%dir %{py_sitescriptdir}/Skype4Py/lang
%{py_sitescriptdir}/Skype4Py/lang/__init__.py[co]

%lang(ar) %{py_sitescriptdir}/Skype4Py/lang/ar.py[co]
%lang(bg) %{py_sitescriptdir}/Skype4Py/lang/bg.py[co]
%lang(cs) %{py_sitescriptdir}/Skype4Py/lang/cs.py[co]
%lang(cz) %{py_sitescriptdir}/Skype4Py/lang/cz.py[co]
%lang(da) %{py_sitescriptdir}/Skype4Py/lang/da.py[co]
%lang(de) %{py_sitescriptdir}/Skype4Py/lang/de.py[co]
%lang(el) %{py_sitescriptdir}/Skype4Py/lang/el.py[co]
%lang(en) %{py_sitescriptdir}/Skype4Py/lang/en.py[co]
%lang(es) %{py_sitescriptdir}/Skype4Py/lang/es.py[co]
%lang(et) %{py_sitescriptdir}/Skype4Py/lang/et.py[co]
%lang(fi) %{py_sitescriptdir}/Skype4Py/lang/fi.py[co]
%lang(fr) %{py_sitescriptdir}/Skype4Py/lang/fr.py[co]
%lang(he) %{py_sitescriptdir}/Skype4Py/lang/he.py[co]
%lang(hu) %{py_sitescriptdir}/Skype4Py/lang/hu.py[co]
%lang(it) %{py_sitescriptdir}/Skype4Py/lang/it.py[co]
%lang(ja) %{py_sitescriptdir}/Skype4Py/lang/ja.py[co]
%lang(ko) %{py_sitescriptdir}/Skype4Py/lang/ko.py[co]
%lang(lt) %{py_sitescriptdir}/Skype4Py/lang/lt.py[co]
%lang(lv) %{py_sitescriptdir}/Skype4Py/lang/lv.py[co]
%lang(nl) %{py_sitescriptdir}/Skype4Py/lang/nl.py[co]
%lang(no) %{py_sitescriptdir}/Skype4Py/lang/no.py[co]
%lang(pl) %{py_sitescriptdir}/Skype4Py/lang/pl.py[co]
%lang(pp) %{py_sitescriptdir}/Skype4Py/lang/pp.py[co]
%lang(pt) %{py_sitescriptdir}/Skype4Py/lang/pt.py[co]
%lang(ro) %{py_sitescriptdir}/Skype4Py/lang/ro.py[co]
%lang(ru) %{py_sitescriptdir}/Skype4Py/lang/ru.py[co]
%lang(sv) %{py_sitescriptdir}/Skype4Py/lang/sv.py[co]
%lang(tr) %{py_sitescriptdir}/Skype4Py/lang/tr.py[co]

%{py_sitescriptdir}/Skype4Py-*.egg-info

%{_examplesdir}/%{name}-%{version}

# urlhandler
%attr(755,root,root) %{_datadir}/skype/skype.py

%files -n kde-protocol-skype
%defattr(644,root,root,755)
%{kde_servicesdir}/skype.protocol

%files -n gnome-urlhandler-skype
%defattr(644,root,root,755)
%{_sysconfdir}/gconf/schemas/skype.schemas
