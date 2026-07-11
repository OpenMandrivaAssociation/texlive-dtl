%global tl_name dtl
%global tl_revision 62387

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6.1
Release:	%{tl_revision}.1
Summary:	Tools to dis-assemble and re-assemble DVI files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/dviware/dtl
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dtl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dtl.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(dtl.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
DTL (DVI Text Language) is a means of expressing the content of a DVI
file, which is readily readable by humans. The DTL bundle contains an
assembler dt2dv (which produces DVI files from DTL files) and a
disassembler dv2dt (which produces DTL files from DVI files). The DTL
bundle was developed so as to avoid some infelicities of dvitype (among
other pressing reasons).

