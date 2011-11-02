Name:		texlive-dtl
Version:	0.6.1
Release:	1
Summary:	Tools to dis-assemble and re-assemble DVI files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/dviware/dtl
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtl.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-dtl.bin
Conflicts:	texlive-texmf <= 20110705-3

%description
DTL (DVI Text Language) is a means of expressing the content of
a DVI file, which is readily readable by humans. The DTL bundle
contains an assembler dt2dv (which produces DVI files from DTL
files) and a disassembler dv2dt (which produces DTL files from
DVI files). The DTL bundle was developed so as to avoid some
infelicities of dvitype (among other pressing reasons).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_mandir}/man1/dt2dv.1*
%{_texmfdir}/doc/man/man1/dt2dv.man1.pdf
%{_mandir}/man1/dv2dt.1*
%{_texmfdir}/doc/man/man1/dv2dt.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
