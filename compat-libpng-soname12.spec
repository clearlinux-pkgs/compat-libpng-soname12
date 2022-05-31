#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF54984BFA16C640F (glennrp+bmo@gmail.com)
#
Name     : compat-libpng-soname12
Version  : 1.2.59
Release  : 26
URL      : https://sourceforge.net/projects/libpng/files/libpng12/1.2.59/libpng-1.2.59.tar.xz
Source0  : https://sourceforge.net/projects/libpng/files/libpng12/1.2.59/libpng-1.2.59.tar.xz
Source1  : https://sourceforge.net/projects/libpng/files/libpng12/1.2.59/libpng-1.2.59.tar.xz.asc
Summary  : Loads and saves PNG files
Group    : Development/Tools
License  : GPL-2.0 Libpng
Requires: compat-libpng-soname12-lib = %{version}-%{release}
Requires: compat-libpng-soname12-license = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gdb
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : zlib-dev32
# Suppress generation of debuginfo
%global debug_package %{nil}

%description
See the note about version numbers near the top of png.h
See INSTALL for instructions on how to install libpng.

%package lib
Summary: lib components for the compat-libpng-soname12 package.
Group: Libraries
Requires: compat-libpng-soname12-license = %{version}-%{release}

%description lib
lib components for the compat-libpng-soname12 package.


%package lib32
Summary: lib32 components for the compat-libpng-soname12 package.
Group: Default
Requires: compat-libpng-soname12-license = %{version}-%{release}

%description lib32
lib32 components for the compat-libpng-soname12 package.


%package license
Summary: license components for the compat-libpng-soname12 package.
Group: Default

%description license
license components for the compat-libpng-soname12 package.


%prep
%setup -q -n libpng-1.2.59
cd %{_builddir}/libpng-1.2.59
pushd ..
cp -a libpng-1.2.59 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634004934
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static --enable-intel-sse
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --enable-intel-sse   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1634004934
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-libpng-soname12
cp %{_builddir}/libpng-1.2.59/LICENSE %{buildroot}/usr/share/package-licenses/compat-libpng-soname12/7d28be2ecb314989578cde33bddb47e208006ed9
cp %{_builddir}/libpng-1.2.59/contrib/gregbook/COPYING %{buildroot}/usr/share/package-licenses/compat-libpng-soname12/dfac199a7539a404407098a2541b9482279f690d
cp %{_builddir}/libpng-1.2.59/contrib/gregbook/LICENSE %{buildroot}/usr/share/package-licenses/compat-libpng-soname12/aa4b9207aaff26bc16c562d6cd766a9eed49af1e
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/bin/libpng-config
rm -f %{buildroot}/usr/bin/libpng12-config
rm -f %{buildroot}/usr/include/libpng12/png.h
rm -f %{buildroot}/usr/include/libpng12/pngconf.h
rm -f %{buildroot}/usr/include/png.h
rm -f %{buildroot}/usr/include/pngconf.h
rm -f %{buildroot}/usr/lib32/libpng.so
rm -f %{buildroot}/usr/lib32/libpng12.so
rm -f %{buildroot}/usr/lib32/pkgconfig/32libpng.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/32libpng12.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/libpng.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/libpng12.pc
rm -f %{buildroot}/usr/lib64/libpng.so
rm -f %{buildroot}/usr/lib64/libpng12.so
rm -f %{buildroot}/usr/lib64/pkgconfig/libpng.pc
rm -f %{buildroot}/usr/lib64/pkgconfig/libpng12.pc
rm -f %{buildroot}/usr/share/man/man3/libpng.3
rm -f %{buildroot}/usr/share/man/man3/libpngpf.3
rm -f %{buildroot}/usr/share/man/man5/png.5

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpng.so.3
/usr/lib64/libpng.so.3.59.0
/usr/lib64/libpng12.so.0
/usr/lib64/libpng12.so.0.59.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libpng.so.3
/usr/lib32/libpng.so.3.59.0
/usr/lib32/libpng12.so.0
/usr/lib32/libpng12.so.0.59.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-libpng-soname12/7d28be2ecb314989578cde33bddb47e208006ed9
/usr/share/package-licenses/compat-libpng-soname12/aa4b9207aaff26bc16c562d6cd766a9eed49af1e
/usr/share/package-licenses/compat-libpng-soname12/dfac199a7539a404407098a2541b9482279f690d
