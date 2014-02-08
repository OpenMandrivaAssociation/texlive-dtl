# revision 26689
# category TLCore
# catalog-ctan /dviware/dtl
# catalog-date 2012-04-09 22:37:34 +0200
# catalog-license pd
# catalog-version 0.6.1
Name:		texlive-dtl
Version:	0.6.1
Release:	4
Summary:	Tools to dis-assemble and re-assemble DVI files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/dviware/dtl
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtl.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-dtl.bin

%description
DTL (DVI Text Language) is a means of expressing the content of
a DVI file, which is readily readable by humans. The DTL bundle
contains an assembler dt2dv (which produces DVI files from DTL
files) and a disassembler dv2dt (which produces DTL files from
DVI files). The DTL bundle was developed so as to avoid some
infelicities of dvitype (among other pressing reasons).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.6.1-3
+ Revision: 812227
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.6.1-2
+ Revision: 751097
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.6.1-1
+ Revision: 718267
- texlive-dtl
- texlive-dtl
- texlive-dtl
- texlive-dtl

