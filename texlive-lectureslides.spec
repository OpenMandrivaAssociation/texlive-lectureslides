Name:		texlive-lectureslides
Version:	62292
Release:	2
Summary:	Combine single PDF files into one file
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lectureslides
License:	cc-by-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lectureslides.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lectureslides.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package makes it easy to combine and index individual PDF
files into one large PDF file.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/lectureslides
%doc %{_texmfdistdir}/doc/latex/lectureslides

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
