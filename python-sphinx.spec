%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}

%define upstream_name Sphinx

Name:           python-sphinx
Version:        0.3
Release:        1%{?dist}
Summary:        Python documentation generator

Group:          Development/Tools
License:        BSD
URL:            http://sphinx.pocoo.org/
Source0:        http://pypi.python.org/packages/source/S/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel python-docutils python-jinja python-setuptools
Requires:       python-docutils python-jinja python-pygments


%description
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

Sphinx uses reStructuredText as its markup language, and many of its
strengths come from the power and straightforwardness of
reStructuredText and its parsing and translating suite, the Docutils.

Although it is still under constant development, the following
features are already present, work fine and can be seen "in action" in
the Python docs:

    * Output formats: HTML (including Windows HTML Help) and LaTeX,
      for printable PDF versions
    * Extensive cross-references: semantic markup and automatic links
      for functions, classes, glossary terms and similar pieces of
      information
    * Hierarchical structure: easy definition of a document tree, with
      automatic links to siblings, parents and children
    * Automatic indices: general index as well as a module index
    * Code handling: automatic highlighting using the Pygments highlighter
    * Various extensions are available, e.g. for automatic testing of
      snippets and inclusion of appropriately formatted docstrings.


%package       doc
Summary:       Documentation for %{name}
Group:         Documentation
License:       BSD
Requires:      %{name} = %{version}-%{release}


%description   doc
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

This package contains documentation in rST and HTML formats


%prep
%setup -q -n %{upstream_name}-%{version}


%build
%{__python} setup.py build
cd doc
make html
mv _build/html ..
rm -rf _*


%install
rm -rf $RPM_BUILD_ROOT
# Fix EOL delimiters
sed -i 's|\r||g' LICENSE
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGES LICENSE README TODO
%{_bindir}/sphinx-*
%{python_sitelib}/sphinx
%if 0%{?fedora} >= 8
%{python_sitelib}/*.egg-info
%endif

%files doc
%defattr(-,root,root,-)
%doc doc html


%changelog
* Mon May 26 2008 Michel Salim <salimma@fedoraproject.org> - 0.3-1
- Update to 0.3

* Fri May  2 2008 Michel Salim <salimma@fedoraproject.org> - 0.1.61950-3
- Split documentation into subpackage
- Exclude C files (not built by default anyway)

* Wed Apr 16 2008 José Matos <jamatos@fc.up.pt> - 0.1.61950-2
- Build html documentation, include it and include the rst
  documentation.

* Thu Mar 27 2008 Michel Salim <michel.sylvan@gmail.com> 0.1.61950-1
- Initial package
