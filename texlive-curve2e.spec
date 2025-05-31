Name:		texlive-curve2e
Version:	72842
Release:	1
Summary:	Extensions for package pict2e
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/curve2e
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/curve2e.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/curve2e.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/curve2e.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/curve2e
%doc %{_texmfdistdir}/doc/latex/curve2e
#- source
%doc %{_texmfdistdir}/source/latex/curve2e

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
