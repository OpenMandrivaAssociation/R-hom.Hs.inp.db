%global packname  hom.Hs.inp.db
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.6.1
Release:          2
Summary:          Homology information for Homo Sapiens from Inparanoid
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              https://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-methods R-AnnotationDbi
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-methods R-AnnotationDbi

%description
Homology information for Homo Sapiens from Inparanoid assembled using data
from public repositories

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# FIXME appears to hang at 100% cpu forever
%if 0
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
