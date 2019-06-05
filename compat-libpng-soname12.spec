#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF54984BFA16C640F (glennrp+bmo@gmail.com)
#
Name     : compat-libpng-soname12
Version  : 1.2.57
Release  : 16
URL      : http://downloads.sourceforge.net/libpng/libpng-1.2.57.tar.xz
Source0  : http://downloads.sourceforge.net/libpng/libpng-1.2.57.tar.xz
Source99 : http://downloads.sourceforge.net/libpng/libpng-1.2.57.tar.xz.asc
Summary  : Loads and saves PNG files
Group    : Development/Tools
License  : GPL-2.0 Libpng
Requires: compat-libpng-soname12-bin
Requires: compat-libpng-soname12-lib
Requires: compat-libpng-soname12-license
Requires: compat-libpng-soname12-man
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gdb
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : zlib-dev32

%description
See the note about version numbers near the top of png.h
See INSTALL for instructions on how to install libpng.

%package bin
Summary: bin components for the compat-libpng-soname12 package.
Group: Binaries
Requires: compat-libpng-soname12-license
Requires: compat-libpng-soname12-man

%description bin
bin components for the compat-libpng-soname12 package.


%package dev
Summary: dev components for the compat-libpng-soname12 package.
Group: Development
Requires: compat-libpng-soname12-lib
Requires: compat-libpng-soname12-bin
Provides: compat-libpng-soname12-devel

%description dev
dev components for the compat-libpng-soname12 package.


%package dev32
Summary: dev32 components for the compat-libpng-soname12 package.
Group: Default
Requires: compat-libpng-soname12-lib32
Requires: compat-libpng-soname12-bin
Requires: compat-libpng-soname12-dev

%description dev32
dev32 components for the compat-libpng-soname12 package.


%package lib
Summary: lib components for the compat-libpng-soname12 package.
Group: Libraries
Requires: compat-libpng-soname12-license

%description lib
lib components for the compat-libpng-soname12 package.


%package lib32
Summary: lib32 components for the compat-libpng-soname12 package.
Group: Default
Requires: compat-libpng-soname12-license

%description lib32
lib32 components for the compat-libpng-soname12 package.


%package license
Summary: license components for the compat-libpng-soname12 package.
Group: Default

%description license
license components for the compat-libpng-soname12 package.


%package man
Summary: man components for the compat-libpng-soname12 package.
Group: Default

%description man
man components for the compat-libpng-soname12 package.


%prep
%setup -q -n libpng-1.2.57
pushd ..
cp -a libpng-1.2.57 build32
popd
pushd ..
cp -a libpng-1.2.57 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531419339
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --enable-intel-sse
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static --enable-intel-sse   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static --enable-intel-sse   --libdir=/usr/lib64/haswell
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1531419339
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/compat-libpng-soname12
cp LICENSE %{buildroot}/usr/share/doc/compat-libpng-soname12/LICENSE
cp contrib/gregbook/COPYING %{buildroot}/usr/share/doc/compat-libpng-soname12/contrib_gregbook_COPYING
cp contrib/gregbook/LICENSE %{buildroot}/usr/share/doc/compat-libpng-soname12/contrib_gregbook_LICENSE
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/libpng-config
%exclude /usr/bin/libpng12-config

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/libpng12/png.h
%exclude /usr/include/libpng12/pngconf.h
%exclude /usr/include/png.h
%exclude /usr/include/pngconf.h
%exclude /usr/lib64/haswell/libpng.so
%exclude /usr/lib64/haswell/libpng12.so
%exclude /usr/lib64/libpng.so
%exclude /usr/lib64/libpng12.so
%exclude /usr/lib64/pkgconfig/libpng.pc
%exclude /usr/lib64/pkgconfig/libpng12.pc

%files dev32
%defattr(-,root,root,-)
%exclude /usr/lib32/libpng.so
%exclude /usr/lib32/libpng12.so
%exclude /usr/lib32/pkgconfig/32libpng.pc
%exclude /usr/lib32/pkgconfig/32libpng12.pc
%exclude /usr/lib32/pkgconfig/libpng.pc
%exclude /usr/lib32/pkgconfig/libpng12.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libpng.so.3
/usr/lib64/haswell/libpng.so.3.57.0
/usr/lib64/haswell/libpng12.so.0
/usr/lib64/haswell/libpng12.so.0.57.0
/usr/lib64/libpng.so.3
/usr/lib64/libpng.so.3.57.0
/usr/lib64/libpng12.so.0
/usr/lib64/libpng12.so.0.57.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libpng.so.3
/usr/lib32/libpng.so.3.57.0
/usr/lib32/libpng12.so.0
/usr/lib32/libpng12.so.0.57.0

%files license
%defattr(-,root,root,-)
%exclude /usr/share/doc/compat-libpng-soname12/LICENSE
%exclude /usr/share/doc/compat-libpng-soname12/contrib_gregbook_COPYING
%exclude /usr/share/doc/compat-libpng-soname12/contrib_gregbook_LICENSE

%files man
%defattr(-,root,root,-)
%exclude /usr/share/man/man3/libpng.3
%exclude /usr/share/man/man3/libpngpf.3
%exclude /usr/share/man/man5/png.5
