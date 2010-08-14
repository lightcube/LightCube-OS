Summary: Packet Capture library
Name: libpcap
Version: 1.1.1
Release: 1
Group: System Environment/Libraries
License: GPL
Distribution: LightCube OS
Vendor: LightCube Solutions
URL: http://www.tcpdump.org
Source: http://dev.lightcube.us/~jhuntwork/sources/%{name}/%{name}-%{version}.tar.gz

Requires: base-layout, glibc
BuildRequires: digest(%{SOURCE0}) = 1bca27d206970badae248cfa471bbb47

%description
libpcap is a Packet Capture library

%package devel
Summary: Headers and libraries for developing with %{name}
Group: Development/Libraries
Requires: %{name}

%description devel
Headers and libraries for developing with %{name}

%prep
%setup -q

%build
./configure \
  --prefix=/usr \
  --libdir=/usr/%{_lib}
make

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
/usr/%{_lib}/libpcap.so.*
/usr/share/man/man5/pcap-savefile.5
/usr/share/man/man7/pcap-filter.7
/usr/share/man/man7/pcap-linktype.7

%files devel
%defattr(-,root,root)
/usr/bin/pcap-config
/usr/include/pcap-bpf.h
/usr/include/pcap-namedb.h
/usr/include/pcap.h
/usr/include/pcap
/usr/%{_lib}/libpcap.a
/usr/%{_lib}/libpcap.so
/usr/share/man/man1/pcap-config.1
/usr/share/man/man3/pcap.3pcap
/usr/share/man/man3/pcap_activate.3pcap
/usr/share/man/man3/pcap_breakloop.3pcap
/usr/share/man/man3/pcap_can_set_rfmon.3pcap
/usr/share/man/man3/pcap_close.3pcap
/usr/share/man/man3/pcap_compile.3pcap
/usr/share/man/man3/pcap_create.3pcap
/usr/share/man/man3/pcap_datalink.3pcap
/usr/share/man/man3/pcap_datalink_name_to_val.3pcap
/usr/share/man/man3/pcap_datalink_val_to_description.3pcap
/usr/share/man/man3/pcap_datalink_val_to_name.3pcap
/usr/share/man/man3/pcap_dispatch.3pcap
/usr/share/man/man3/pcap_dump.3pcap
/usr/share/man/man3/pcap_dump_close.3pcap
/usr/share/man/man3/pcap_dump_file.3pcap
/usr/share/man/man3/pcap_dump_flush.3pcap
/usr/share/man/man3/pcap_dump_fopen.3pcap
/usr/share/man/man3/pcap_dump_ftell.3pcap
/usr/share/man/man3/pcap_dump_open.3pcap
/usr/share/man/man3/pcap_file.3pcap
/usr/share/man/man3/pcap_fileno.3pcap
/usr/share/man/man3/pcap_findalldevs.3pcap
/usr/share/man/man3/pcap_fopen_offline.3pcap
/usr/share/man/man3/pcap_free_datalinks.3pcap
/usr/share/man/man3/pcap_freealldevs.3pcap
/usr/share/man/man3/pcap_freecode.3pcap
/usr/share/man/man3/pcap_get_selectable_fd.3pcap
/usr/share/man/man3/pcap_geterr.3pcap
/usr/share/man/man3/pcap_getnonblock.3pcap
/usr/share/man/man3/pcap_inject.3pcap
/usr/share/man/man3/pcap_is_swapped.3pcap
/usr/share/man/man3/pcap_lib_version.3pcap
/usr/share/man/man3/pcap_list_datalinks.3pcap
/usr/share/man/man3/pcap_lookupdev.3pcap
/usr/share/man/man3/pcap_lookupnet.3pcap
/usr/share/man/man3/pcap_loop.3pcap
/usr/share/man/man3/pcap_major_version.3pcap
/usr/share/man/man3/pcap_minor_version.3pcap
/usr/share/man/man3/pcap_next.3pcap
/usr/share/man/man3/pcap_next_ex.3pcap
/usr/share/man/man3/pcap_offline_filter.3pcap
/usr/share/man/man3/pcap_open_dead.3pcap
/usr/share/man/man3/pcap_open_live.3pcap
/usr/share/man/man3/pcap_open_offline.3pcap
/usr/share/man/man3/pcap_perror.3pcap
/usr/share/man/man3/pcap_sendpacket.3pcap
/usr/share/man/man3/pcap_set_buffer_size.3pcap
/usr/share/man/man3/pcap_set_datalink.3pcap
/usr/share/man/man3/pcap_set_promisc.3pcap
/usr/share/man/man3/pcap_set_rfmon.3pcap
/usr/share/man/man3/pcap_set_snaplen.3pcap
/usr/share/man/man3/pcap_set_timeout.3pcap
/usr/share/man/man3/pcap_setdirection.3pcap
/usr/share/man/man3/pcap_setfilter.3pcap
/usr/share/man/man3/pcap_setnonblock.3pcap
/usr/share/man/man3/pcap_snapshot.3pcap
/usr/share/man/man3/pcap_stats.3pcap
/usr/share/man/man3/pcap_statustostr.3pcap
/usr/share/man/man3/pcap_strerror.3pcap

%changelog
* Thu Aug 12 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 1.1.1-1
- Initial version