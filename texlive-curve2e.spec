# revision 25569
# category Package
# catalog-ctan /macros/latex/contrib/curve2e
# catalog-date 2012-03-05 13:28:31 +0100
# catalog-license lppl1.3
# catalog-version 1.4
Name:		texlive-curve2e
Version:	1.40
Release:	3
Summary:	Extensions for package pict2e
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/curve2e
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/curve2e.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/curve2e.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/curve2e.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package extends the drawing capacities of the pict2e that
serves as a LaTeX 2e replacement for picture mode. In
particular, curve2e introduces new macros for lines and
vectors, new specifications for line terminations and joins,
arcs with any angular aperture, arcs with arrows at one or both
ends, generic curves specified with their nodes and the tangent
direction at these nodes.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/curve2e/curve2e.sty
%doc %{_texmfdistdir}/doc/latex/curve2e/README
%doc %{_texmfdistdir}/doc/latex/curve2e/curve2e.pdf
%doc %{_texmfdistdir}/doc/latex/curve2e/manifest.txt
#- source
%doc %{_texmfdistdir}/source/latex/curve2e/curve2e.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.40-2
+ Revision: 783481
- rebuild without scriptlet dependencies

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.40-1
+ Revision: 782986
- Update to latest release.
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.31-2
+ Revision: 750752
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.31-1
+ Revision: 718189
- texlive-curve2e
- texlive-curve2e
- texlive-curve2e
- texlive-curve2e

