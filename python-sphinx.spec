%if 0%{?fedora}
%global with_python3 1
%else
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

%global upstream_name Sphinx

Name:       python-sphinx
Version:    1.3.1
Release:    1%{?dist}
Summary:    Python documentation generator

Group:      Development/Tools

# Unless otherwise noted, the license for code is BSD
# sphinx/util/stemmer.py Public Domain
# sphinx/pycode/pgen2 Python
# jquery (MIT or GPLv2)
License:    BSD and Public Domain and Python and (MIT or GPLv2)
URL:        http://sphinx-doc.org/
Source0:    http://pypi.python.org/packages/source/S/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
Patch0:     Sphinx-1.2.1-mantarget.patch

BuildArch:     noarch
BuildRequires: python2-devel >= 2.4
BuildRequires: python-babel
BuildRequires: python-setuptools
BuildRequires: python-docutils
BuildRequires: python-jinja2
BuildRequires: python-pygments >= 2.0
BuildRequires: python-six
BuildRequires: python-sphinx_rtd_theme
BuildRequires: python2-sphinx-theme-alabaster

# for fixes
BuildRequires: dos2unix

# for testing
BuildRequires: python-nose
BuildRequires: gettext
BuildRequires: texinfo
BuildRequires: python-sqlalchemy
BuildRequires: python-whoosh
BuildRequires: python2-snowballstemmer
# note: no Python3 xapian binding yet
BuildRequires: xapian-bindings-python
BuildRequires: texlive-collection-fontsrecommended
BuildRequires: texlive-collection-latex
BuildRequires: tex(cmap.sty)
BuildRequires: tex(ecrm1000.tfm)
BuildRequires: tex(fancybox.sty)
BuildRequires: tex(footnote.sty)
BuildRequires: tex(framed.sty)
BuildRequires: tex(multirow.sty)
BuildRequires: tex(parskip.sty)
BuildRequires: tex(titlesec.sty)
BuildRequires: tex(threeparttable.sty)
BuildRequires: tex(upquote.sty)
BuildRequires: tex(wrapfig.sty)


%if 0%{?with_python3}
BuildRequires: python3-devel
BuildRequires: python3-babel
BuildRequires: python3-setuptools
BuildRequires: python3-docutils
BuildRequires: python3-jinja2
BuildRequires: python3-pygments
BuildRequires: python3-nose
BuildRequires: python3-sqlalchemy
BuildRequires: python3-whoosh
BuildRequires: python3-snowballstemmer
BuildRequires: python3-six
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-sphinx-theme-alabaster
%endif # with_python3


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


%package -n    python2-%{upstream_name}
Summary:       Python documentation generator
Requires:      python-babel
Requires:      python-docutils
Requires:      python-jinja2
Requires:      python-pygments
Requires:      python2-snowballstemmer
Requires:      python2-sphinx_rtd_theme
Requires:      python-sphinx_rtd_theme
Requires:      python2-six
Obsoletes:     python-sphinx = 1.2.3
%{?python_provide:%python_provide python2-sphinx}

%description -n python2-%{upstream_name}
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


%package latex
Summary:       LaTeX builder dependencies for %{name}
Requires:      %{name} = %{version}-%{release}
Requires:      texlive-collection-fontsrecommended
Requires:      texlive-collection-latex
Requires:      tex(cmap.sty)
Requires:      tex(ecrm1000.tfm)
Requires:      tex(fancybox.sty)
Requires:      tex(footnote.sty)
Requires:      tex(framed.sty)
Requires:      tex(multirow.sty)
Requires:      tex(parskip.sty)
Requires:      tex(titlesec.sty)
Requires:      tex(threeparttable.sty)
Requires:      tex(upquote.sty)
Requires:      tex(wrapfig.sty)

%description latex
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

This package pulls in the TeX dependencies needed by Sphinx's LaTeX
builder.


%if 0%{?with_python3}
%package -n python3-sphinx
Summary:       Python documentation generator
Group:         Development/Tools
Requires:      python-babel
Requires:      python3-docutils
Requires:      python3-jinja2
Requires:      python3-pygments
Requires:      python3-snowballstemmer
Requires:      python3-sphinx_rtd_theme
Requires:      python3-sphinx-theme-alabaster
Requires:      python3-six
%{?python_provide:%python_provide python3-sphinx}

%description -n python3-sphinx
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

%package -n python3-sphinx-latex
Summary:       LaTeX builder dependencies for %{name}
Requires:      python3-sphinx = %{version}-%{release}
Requires:      texlive-collection-fontsrecommended
Requires:      texlive-collection-latex
Requires:      tex(cmap.sty)
Requires:      tex(ecrm1000.tfm)
Requires:      tex(fancybox.sty)
Requires:      tex(footnote.sty)
Requires:      tex(framed.sty)
Requires:      tex(multirow.sty)
Requires:      tex(parskip.sty)
Requires:      tex(titlesec.sty)
Requires:      tex(threeparttable.sty)
Requires:      tex(upquote.sty)
Requires:      tex(wrapfig.sty)

%description -n python3-sphinx-latex
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

This package pulls in the TeX dependencies needed by Sphinx's LaTeX
builder.
%endif # with_python3


%package doc
Summary:    Documentation for %{name}
Group:      Documentation
License:    BSD
Requires:   %{name} = %{version}-%{release}

%description doc
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

This package contains documentation in reST and HTML formats.


%prep
%autosetup -n %{upstream_name}-%{version}%{?prerel} -p1

sed '1d' -i sphinx/pycode/pgen2/token.py

# fix line encoding of bundled jquery.js
dos2unix -k ./sphinx/themes/basic/static/jquery.js

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3


%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif # with_python3

pushd doc
make html
make man
rm -rf _build/html/.buildinfo
mv _build/html ..
popd


%install
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python3 version
# to be the default for now).
%py2_install
for f in %{buildroot}%{_bindir}/sphinx-*;
do
    mv $f $f-%{python2_version}
    ln -s %{_bindir}/`basename $f-%{python2_version}` $f-2
done


%if 0%{?with_python3}
%py3_install
%endif # with_python3


pushd doc
# Deliver man pages
install -d %{buildroot}%{_mandir}/man1
mv _build/man/sphinx-*.1 %{buildroot}%{_mandir}/man1/
for f in %{buildroot}%{_mandir}/man1/sphinx-*.1;
do
    cp -p $f $(echo $f | sed -e "s|.1$|-%{python2_version}.1|")
done

# Remove language files, they're identical to the ones from the
# Python 2 build that will be moved to /usr/share below
find %{buildroot}%{python3_sitelib}/sphinx/locale -maxdepth 1 -mindepth 1 -type d -not -path '*/\.*' -exec rm -rf '{}' \;
popd

# Deliver rst files
rm -rf doc/_build
sed -i 's|python ../sphinx-build.py|/usr/bin/sphinx-build|' doc/Makefile
mv doc reST

# Move language files to /usr/share;
# patch to support this incorporated in 0.6.6
pushd %{buildroot}%{python_sitelib}

for lang in `find sphinx/locale -maxdepth 1 -mindepth 1 -type d -not -path '*/\.*' -printf "%f "`;
do
  install -d %{buildroot}%{_datadir}/sphinx/locale/$lang
  install -d %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
  mv sphinx/locale/$lang/LC_MESSAGES/sphinx.js \
     %{buildroot}%{_datadir}/sphinx/locale/$lang/
  mv sphinx/locale/$lang/LC_MESSAGES/sphinx.mo \
    %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
  rm -rf sphinx/locale/$lang
done
popd
%find_lang sphinx

# Language files; Since these are javascript, it's not immediately obvious to
# find_lang that they need to be marked with a language.
(cd %{buildroot} && find . -name 'sphinx.js') | sed -e 's|^.||' | sed -e \
  's:\(.*/locale/\)\([^/_]\+\)\(.*\.js$\):%lang(\2) \1\2\3:' \
  >> sphinx.lang


%check
LANG=en_US.UTF-8 make test
%if 0%{?with_python3}
pushd %{py3dir}
LANG=en_US.UTF-8 PYTHON=python3 make test
popd
%endif # with_python3


%files -f sphinx.lang -n python2-%{upstream_name}
%license LICENSE
%doc AUTHORS CHANGES EXAMPLES README.rst
%{_bindir}/sphinx-*-2
%{_bindir}/sphinx-*-%{python2_version}
%{python2_sitelib}/sphinx/
%{python2_sitelib}/Sphinx-%{version}-py%{python2_version}.egg-info/
%dir %{_datadir}/sphinx/
%dir %{_datadir}/sphinx/locale
%dir %{_datadir}/sphinx/locale/*
%{_mandir}/man1/sphinx-*-%{python2_version}.1*

%files latex
%license LICENSE

%if 0%{?with_python3}
%files -n python3-sphinx -f sphinx.lang
%license LICENSE
%doc AUTHORS CHANGES EXAMPLES README.rst
%exclude %{_bindir}/sphinx-*-2
%exclude %{_bindir}/sphinx-*-%{python2_version}
%{_bindir}/sphinx*
%{python3_sitelib}/sphinx/
%{python3_sitelib}/Sphinx-%{version}-py%{python3_version}.egg-info/
%dir %{_datadir}/sphinx/
%dir %{_datadir}/sphinx/locale
%dir %{_datadir}/sphinx/locale/*
%exclude %{_mandir}/man1/sphinx-*-%{python2_version}.1*
%{_mandir}/man1/*

%files -n python3-sphinx-latex
%license LICENSE
%endif # with_python3

%files doc
%doc html reST


%changelog
* Tue Nov 24 2015 Julien Enselme <jujens@jujens.eu> - 1.3.1-1
- Update to 1.3.1
- Update to new guidelines
- Make the default executable use python3

* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 1.2.3-5
- Rebuilt for Python3.5 rebuild
- add patch to reflect that Python3.5 dropped HTMLParserError

* Mon Jul 20 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.2.3-4
- Fix line encoding of bundled jquery.js

* Mon Jul 20 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.2.3-3
- Re-introduce LaTeX subpackage, solely for pulling in LaTeX dependencies

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb  5 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3
- Mark license file with %%license instead of %%doc

* Thu Feb  5 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.2.2-10
- Complete LaTeX builder deps (fixes bz#882166)
- Make test output verbose
- Add BRs needed to enable all tests

* Tue Feb  3 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.2.2-9
- python3-sphinx package also Provides: python3-sphinx-latex

* Tue Feb  3 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.2.2-8
- If a separate LaTeX subpackage is not generated, the main package should have
  a virtual Provides: for it (bz#1187989)

* Tue Jan 27 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.2.2-7
- Disable separate LaTeX builder for now (bz#1185574)

* Thu Jan 22 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.2.2-6
- Split off LaTeX builder into its own subpackages, to remove TeXLive
  dependencies from the main package.
  Thanks to Robert Kuska <rkuska@redhat.com> for feedback
- Clean up python3-sphinx's locale files, they ended up in the python2 package.
  Share the locale files in /usr/share instead

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.2-4
- Don't own the -3 scripts by python 2 package

* Thu May 22 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.2-3
- Add sphinx-*-3 links to scripts
Resolves: #1098109

* Fri May  9 2014 Orion Poplawski <orion@cora.nwra.com> - 1.2.2-2
- Rebuild for Python 3.4

* Fri May  9 2014 Orion Poplawski <orion@cora.nwra.com> - 1.2.2-1
- Update to 1.2.2

* Thu Feb 13 2014 Michel Salim <salimma@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar  9 2013 Michel Salim <salimma@fedoraproject.org> - 1.1.3-7
- Fix inheritance_diagram quoting bug, exposed by the newer, stricter dot

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 21 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1.3-5
- Fix for use of sphinx's manpage writer with docutils-0.10

* Mon Aug  6 2012 Michel Salim <salimma@fedoraproject.org> - 1.1.3-4
- Rebuild for Python 3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 1.1.3-3
- remove rhel logic from with_python3 conditional

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr  5 2012 Michel Salim <salimma@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3

* Sun Feb  5 2012 Michel Salim <salimma@fedoraproject.org> - 1.1.2-5
- Move python3 runtime dependencies to the right subpackage
- Properly exclude python3 binaries

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 17 2011 Michel Salim <salimma@fedoraproject.org> - 1.1.2-3
- BR on texlive-latex for LaTeX tests

* Thu Dec  8 2011 Michel Salim <salimma@fedoraproject.org> - 1.1.2-2
- Enable python3 subpackage

* Mon Nov 28 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1.2-1
- Update to upstream 1.1.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0.7-1
- Update to upstream 1.0.7

* Mon Jan 17 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0.6-1
- Update to upstream 1.0.6

* Mon Nov  1 2010 Michel Salim <salimma@fedoraproject.org> - 1.0.4-3
- Fix -doc Makefile to allow regeneration of .rst files

* Mon Nov  1 2010 Michel Salim <salimma@fedoraproject.org> - 1.0.4-2
- Actually include *.js locale files
- Generate manpages

* Fri Sep 17 2010 Michel Salim <salimma@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4
- Remove BuildRoot and %%clean declarations

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.0-0.1.b2.1
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon May 31 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0-0.2.b2
- Update to 1.0 beta 2
- Fixes problem building html documentation in non-English locales

* Wed May 26 2010 Michel Salim <salimma@fedoraproject.org> - 1.0-0.1.b1
- Update to 1.0 beta 1

* Tue May 25 2010 Michel Salim <salimma@fedoraproject.org> - 0.6.6-1
- Update to 0.6.6

* Fri May 21 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.5-2
- Few minor tweaks to Gareth's spec file update

* Mon May 10 2010 Gareth Armstrong <gareth.armstrong@hp.com> - 0.6.5-1.hp
- Update to 0.6.5
- Initial import of python-sphinx from Fedora Rawhide for use in HP CMS
- Enforce that Sphinx requires Python 2.4 or later via an explicit BR
- Minor tweaks to spec file
- Move language files to %%{_datadir}, idea borrowed from Debian's sphinx
  package
- Deliver man pages for sphinx-build & sphinx-quickstart
- Deliver rst documentation files to reST directory in doc sub-package
- Add %%check section for Python2 and add BR on python-nose

* Wed Jan 13 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.4-1
- Update to 0.6.4
- Fixes a problem using autodoc with pylons projects.

* Fri Sep  4 2009 Michel Salim <salimma@fedoraproject.org> - 0.6.3-1
- Update to 0.6.3

* Mon Aug 17 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2 -- upstream bugfix requested inside bz#512438

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 05 2009 Luke Macken <lmacken@redhat.com> - 0.6.1-2
- Add a patch to use our own setuptools package

* Fri Apr 17 2009 Michel Salim <salimma@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan  2 2009 Michel Salim <salimma@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.5-2
- Rebuild for Python 2.6

* Mon Nov 24 2008 Michel Salim <salimma@fedoraproject.org> - 0.5-1
- Update to 0.5

* Fri Oct 10 2008 Michel Salim <salimma@fedoraproject.org> - 0.4.3-1
- Update to 0.4.3

* Wed Aug 27 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.4.2-1.1
- Fix for EL-5 build.

* Mon Aug 25 2008 Michel Salim <salimma@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

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
