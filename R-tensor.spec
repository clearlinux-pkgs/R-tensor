#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tensor
Version  : 1.5
Release  : 41
URL      : https://cran.r-project.org/src/contrib/tensor_1.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tensor_1.5.tar.gz
Summary  : Tensor product of arrays
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
product of the arrays collapsed in specific extents by summing
        along the appropriate diagonals.

%prep
%setup -q -c -n tensor
cd %{_builddir}/tensor

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641135959

%install
export SOURCE_DATE_EPOCH=1641135959
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tensor
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tensor
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tensor
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc tensor || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tensor/DESCRIPTION
/usr/lib64/R/library/tensor/INDEX
/usr/lib64/R/library/tensor/Meta/Rd.rds
/usr/lib64/R/library/tensor/Meta/features.rds
/usr/lib64/R/library/tensor/Meta/hsearch.rds
/usr/lib64/R/library/tensor/Meta/links.rds
/usr/lib64/R/library/tensor/Meta/nsInfo.rds
/usr/lib64/R/library/tensor/Meta/package.rds
/usr/lib64/R/library/tensor/NAMESPACE
/usr/lib64/R/library/tensor/R/tensor
/usr/lib64/R/library/tensor/R/tensor.rdb
/usr/lib64/R/library/tensor/R/tensor.rdx
/usr/lib64/R/library/tensor/help/AnIndex
/usr/lib64/R/library/tensor/help/aliases.rds
/usr/lib64/R/library/tensor/help/paths.rds
/usr/lib64/R/library/tensor/help/tensor.rdb
/usr/lib64/R/library/tensor/help/tensor.rdx
/usr/lib64/R/library/tensor/html/00Index.html
/usr/lib64/R/library/tensor/html/R.css
