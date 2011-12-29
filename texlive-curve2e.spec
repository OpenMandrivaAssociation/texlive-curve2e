# revision 23482
# category Package
# catalog-ctan /macros/latex/contrib/curve2e
# catalog-date 2011-07-29 16:36:04 +0200
# catalog-license lppl1.3
# catalog-version 1.31
Name:		texlive-curve2e
Version:	1.31
Release:	1
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
