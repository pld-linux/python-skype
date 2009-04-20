%define 	module	skype
Summary:	Python wrapper for the Skype API
Name:		python-%{module}
Version:	1.0.31.0
Release:	0.1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/skype4py/Skype4Py-%{version}.tar.gz
# Source0-md5:	13091fccca8160e3e51ec064f42c82fd
URL:		https://developer.skype.com/wiki/Skype4Py
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Skype4Py is a Python wrapper for the Skype API. It is platform
independant, written completly in Python and reimplements the
Skype4COM's API in a pythonic way.

%prep
%setup -q -n Skype4Py-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%dir %{py_sitescriptdir}/Skype4Py
%{py_sitescriptdir}/Skype4Py/*.py[co]
%dir %{py_sitescriptdir}/Skype4Py/API
%{py_sitescriptdir}/Skype4Py/API/*.py[co]
%dir %{py_sitescriptdir}/Skype4Py/Languages
%{py_sitescriptdir}/Skype4Py/Languages/__init__.py[co]

%lang(ar) %{py_sitescriptdir}/Skype4Py/Languages/ar.py[co]
%lang(bg) %{py_sitescriptdir}/Skype4Py/Languages/bg.py[co]
%lang(cs) %{py_sitescriptdir}/Skype4Py/Languages/cs.py[co]
%lang(cz) %{py_sitescriptdir}/Skype4Py/Languages/cz.py[co]
%lang(da) %{py_sitescriptdir}/Skype4Py/Languages/da.py[co]
%lang(de) %{py_sitescriptdir}/Skype4Py/Languages/de.py[co]
%lang(el) %{py_sitescriptdir}/Skype4Py/Languages/el.py[co]
%lang(en) %{py_sitescriptdir}/Skype4Py/Languages/en.py[co]
%lang(es) %{py_sitescriptdir}/Skype4Py/Languages/es.py[co]
%lang(et) %{py_sitescriptdir}/Skype4Py/Languages/et.py[co]
%lang(fi) %{py_sitescriptdir}/Skype4Py/Languages/fi.py[co]
%lang(fr) %{py_sitescriptdir}/Skype4Py/Languages/fr.py[co]
%lang(he) %{py_sitescriptdir}/Skype4Py/Languages/he.py[co]
%lang(hu) %{py_sitescriptdir}/Skype4Py/Languages/hu.py[co]
%lang(it) %{py_sitescriptdir}/Skype4Py/Languages/it.py[co]
%lang(ja) %{py_sitescriptdir}/Skype4Py/Languages/ja.py[co]
%lang(ko) %{py_sitescriptdir}/Skype4Py/Languages/ko.py[co]
%lang(lt) %{py_sitescriptdir}/Skype4Py/Languages/lt.py[co]
%lang(lv) %{py_sitescriptdir}/Skype4Py/Languages/lv.py[co]
%lang(nl) %{py_sitescriptdir}/Skype4Py/Languages/nl.py[co]
%lang(no) %{py_sitescriptdir}/Skype4Py/Languages/no.py[co]
%lang(pl) %{py_sitescriptdir}/Skype4Py/Languages/pl.py[co]
%lang(pp) %{py_sitescriptdir}/Skype4Py/Languages/pp.py[co]
%lang(pt) %{py_sitescriptdir}/Skype4Py/Languages/pt.py[co]
%lang(ro) %{py_sitescriptdir}/Skype4Py/Languages/ro.py[co]
%lang(ru) %{py_sitescriptdir}/Skype4Py/Languages/ru.py[co]
%lang(sv) %{py_sitescriptdir}/Skype4Py/Languages/sv.py[co]
%lang(tr) %{py_sitescriptdir}/Skype4Py/Languages/tr.py[co]
# ???
%lang(x1) %{py_sitescriptdir}/Skype4Py/Languages/x1.py[co]

%{py_sitescriptdir}/Skype4Py-*.egg-info