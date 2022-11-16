Name:		texlive-luamathalign
Version:	63226
Release:	1
Summary:	More flexible alignment in amsmath environments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/luamathalign
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luamathalign.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luamathalign.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luamathalign.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Allow aligning mathematical expressions on points where where
direcly using & is not possible, especially in nested macros or
environments.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/lualatex/luamathalign
%{_texmfdistdir}/tex/lualatex/luamathalign
%doc %{_texmfdistdir}/doc/lualatex/luamathalign

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
