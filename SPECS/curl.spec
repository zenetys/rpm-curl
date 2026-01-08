# Supported targets: el8, el9, el10

%define _prefix /opt/%{name}
%define _docdir_fmt curl

%{!?make_verbose: %define make_verbose 0}

%global source_date_epoch_from_changelog 0

# el10 adds /usr/lib/rpm/check-rpaths which won't pass because we use
# non-standard rpaths for aws-lc, ngtcp2 and nghttp3 libraries, which
# is on purpose
%global __brp_check_rpaths %{nil}

Name: curl0z
Version: 8.18.0
Release: 1%{?dist}.zenetys
Summary: curl command line tool and library
License: MIT
URL: https://curl.se

Source0: https://curl.haxx.se/download/curl-%{version}.tar.xz

BuildRequires: aws-lc-0z-devel
BuildRequires: gcc
BuildRequires: krb5-devel
BuildRequires: libnghttp2-devel
BuildRequires: make
BuildRequires: nghttp3-0z-devel
BuildRequires: ngtcp2-0z-devel
BuildRequires: perl-interpreter
BuildRequires: zlib-devel

Requires: aws-lc-0z
Requires: krb5-libs
Requires: libnghttp2
Requires: nghttp3-0z
Requires: ngtcp2-0z

%description
curl command line tool and library for getting or sending data
using URL syntax.

%prep
%setup -n curl-%{version}

%build
libs=(
    '%{aws_lc_0z_prefix}/%{_lib}'
    '%{ngtcp2_0z_prefix}/%{_lib}'
    '%{nghttp3_0z_prefix}/%{_lib}'
)
pkg_config_path=$(IFS=:; echo "${libs[*]/%//pkgconfig}")
ldflags=-Wl,-rpath,%{_libdir}:$(IFS=:; echo "${libs[*]}")

%configure \
    --disable-dict \
    --disable-gopher \
    --disable-hsts \
    --disable-imap \
    --enable-ipv6 \
    --enable-kerberos-auth \
    --disable-ldap \
    --disable-ldaps \
    --enable-manual \
    --disable-mqtt \
    --enable-ntlm \
    --disable-pop3 \
    --disable-rtsp \
    --disable-smb \
    --disable-smtp \
    --disable-static \
    --enable-symbol-hiding \
    --disable-telnet \
    --enable-threaded-resolver \
    --disable-tftp \
    --disable-tls-srp \
    --without-brotli \
    --with-ca-bundle=/etc/pki/tls/certs/ca-bundle.crt \
    --with-gssapi \
    --without-libgsasl \
    --without-libidn2 \
    --without-libpsl \
    --without-libssh \
    --with-nghttp2 \
    --with-nghttp3=%{nghttp3_0z_prefix} \
    --with-ngtcp2=%{ngtcp2_0z_prefix} \
    --with-openssl=%{aws_lc_0z_prefix} \
    --with-ssl \
    --without-zstd \
    PKG_CONFIG_PATH="$pkg_config_path" \
    LDFLAGS="$ldflags"

%make_build V=%{make_verbose}

%install
%make_install

rm -f %{buildroot}%{_prefix}/%{_lib}/libcurl.la

mkdir -p %{buildroot}%{_rpmmacrodir}
echo '%%%(echo %{name} |tr '-' '_')_prefix %{_prefix}' \
    > %{buildroot}%{_rpmmacrodir}/macros.%{name}

%files
%doc README
%doc RELEASE-NOTES
%doc docs/BUGS.md
%doc docs/FAQ.md
%doc docs/FEATURES.md
%doc docs/TODO.md
%doc docs/TheArtOfHttpScripting.md
%license COPYING

%{_bindir}/curl
%{_bindir}/wcurl
%{_libdir}/libcurl.so.*
%{_mandir}/man1/curl.1*
%{_mandir}/man1/wcurl.1*

%package devel
Summary: curl development files from package %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
curl development files from package %{name}.

%files devel
%{_bindir}/curl-config
%{_datadir}/aclocal/libcurl.m4
%{_includedir}/curl
%{_libdir}/libcurl.so
%{_libdir}/pkgconfig/libcurl.pc
%{_mandir}/man1/curl-config.1*
%{_mandir}/man3/*
%{_rpmmacrodir}/macros.%{name}
