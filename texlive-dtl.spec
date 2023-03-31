Name:		texlive-dtl
Version:	62387
Release:	2
Summary:	Tools to dis-assemble and re-assemble DVI files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/dviware/dtl
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtl.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-dtl.bin

%description
DTL (DVI Text Language) is a means of expressing the content of
a DVI file, which is readily readable by humans. The DTL bundle
contains an assembler dt2dv (which produces DVI files from DTL
files) and a disassembler dv2dt (which produces DTL files from
DVI files). The DTL bundle was developed so as to avoid some
infelicities of dvitype (among other pressing reasons).

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/dt2dv.1*
%doc %{_texmfdistdir}/doc/man/man1/dt2dv.man1.pdf
%doc %{_mandir}/man1/dv2dt.1*
%doc %{_texmfdistdir}/doc/man/man1/dv2dt.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
