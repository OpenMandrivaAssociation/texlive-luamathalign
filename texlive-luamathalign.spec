%global tl_name luamathalign
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	More flexible alignment in amsmath environments
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/luamathalign
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luamathalign.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luamathalign.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luamathalign.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Allow aligning mathematical expressions on points where directly using &
is not possible, especially in nested macros or environments.

