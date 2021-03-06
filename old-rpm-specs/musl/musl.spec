Summary: musl
Name: musl
Version: 0.8.9
Release: 1
Group: System Environment/Libraries
License: GPLv2
Distribution: LightCube OS
Vendor: LightCube Solutions
URL: http://www.etalabs.net/musl
Source0: http://www.etalabs.net/musl/releases/%{name}-%{version}.tar.gz
Source1: musl-config

BuildRequires: digest(sha1:%{SOURCE0}) = 7fe4e6d3e91968ed7490259ae5a2b9c61e82743b
BuildRequires: digest(sha1:%{SOURCE1}) = 4e1ba96338fa03ddbb767c27fe7a26763c391a3c

%description
musl, pronounced like "mussel" or "muscle", is an implementation of the C/POSIX
standard library intended for use on Linux-based systems. musl is lightweight,
fast, simple, free, and strives to be correct in the sense of standards-
conformance and safety.

%package devel
Summary: Headers, object files and utilities for development using C libraries
Group: Development/Libraries
Requires: %{name} >= %{version}

%description devel
The %{name}-devel package contains the object files necessary for
developing programs which use the standard C libraries (which are used
by nearly all programs).  If you are developing programs which will use
the standard C libraries, your system needs to have these standard
object files available in order to create the executables.

%prep
%setup -q
echo "
#undef powerof2
#define powerof2(x) ((((x) - 1) & (x)) == 0)
" >> include/sys/param.h

%build
cp %{SOURCE1} config.mak
make %{PMFLAGS}

%install
make DESTDIR=%{buildroot} install
install -d %{buildroot}/lib
# Remove headers provided by the kernel
rm -rf %{buildroot}/include/linux
ln -sf libc.so %{buildroot}/lib/ld-musl-%{_arch}.so.1
%{strip}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/lib/libc.so
/lib/ld-musl-%{_arch}.so.1

%files devel
%defattr(-,root,root)
/lib/libc.a
/bin/musl-gcc
/include/aio.h
/include/alloca.h
%dir /include/arpa
/include/arpa/inet.h
/include/arpa/nameser.h
/include/arpa/telnet.h
/include/assert.h
%dir /include/bits
/include/bits/alltypes.h
/include/bits/endian.h
/include/bits/errno.h
/include/bits/fcntl.h
/include/bits/fenv.h
/include/bits/float.h
/include/bits/ioctl.h
/include/bits/ipc.h
/include/bits/limits.h
/include/bits/mman.h
/include/bits/msg.h
/include/bits/posix.h
/include/bits/reg.h
/include/bits/setjmp.h
/include/bits/shm.h
/include/bits/signal.h
/include/bits/socket.h
/include/bits/stat.h
/include/bits/statfs.h
/include/bits/stdarg.h
/include/bits/stdint.h
/include/bits/syscall.h
/include/bits/termios.h
/include/bits/user.h
/include/bits/wchar.h
/include/byteswap.h
/include/complex.h
/include/cpio.h
/include/ctype.h
/include/dirent.h
/include/dlfcn.h
/include/elf.h
/include/endian.h
/include/err.h
/include/errno.h
/include/fcntl.h
/include/features.h
/include/fenv.h
/include/float.h
/include/fnmatch.h
/include/ftw.h
/include/getopt.h
/include/glob.h
/include/grp.h
/include/iconv.h
/include/inttypes.h
/include/iso646.h
/include/langinfo.h
/include/libgen.h
/include/libintl.h
/include/limits.h
/include/locale.h
/include/malloc.h
/include/math.h
/include/memory.h
/include/mntent.h
/include/monetary.h
/include/mqueue.h
%dir /include/net
/include/net/ethernet.h
/include/net/if.h
/include/net/if_arp.h
/include/net/route.h
/include/netdb.h
%dir /include/netinet
/include/netinet/icmp6.h
/include/netinet/if_ether.h
/include/netinet/in.h
/include/netinet/ip.h
/include/netinet/ip6.h
/include/netinet/ip_icmp.h
/include/netinet/tcp.h
/include/netinet/udp.h
%dir /include/netpacket
/include/netpacket/packet.h
/include/nl_types.h
/include/paths.h
/include/poll.h
/include/pthread.h
/include/pty.h
/include/pwd.h
/include/regex.h
/include/resolv.h
/include/sched.h
/include/search.h
/include/semaphore.h
/include/setjmp.h
/include/shadow.h
/include/signal.h
/include/spawn.h
/include/stdarg.h
/include/stdbool.h
/include/stddef.h
/include/stdint.h
/include/stdio.h
/include/stdio_ext.h
/include/stdlib.h
/include/string.h
/include/strings.h
/include/stropts.h
%dir /include/sys
/include/sys/epoll.h
/include/sys/eventfd.h
/include/sys/inotify.h
/include/sys/file.h
/include/sys/fsuid.h
/include/sys/ioctl.h
/include/sys/ipc.h
/include/sys/kd.h
/include/sys/klog.h
/include/sys/mman.h
/include/sys/mount.h
/include/sys/msg.h
/include/sys/param.h
/include/sys/poll.h
/include/sys/prctl.h
/include/sys/procfs.h
/include/sys/ptrace.h
/include/sys/reboot.h
/include/sys/reg.h
/include/sys/resource.h
/include/sys/select.h
/include/sys/sem.h
/include/sys/sendfile.h
/include/sys/shm.h
/include/sys/signalfd.h
/include/sys/socket.h
/include/sys/soundcard.h
/include/sys/stat.h
/include/sys/statfs.h
/include/sys/statvfs.h
/include/sys/stropts.h
/include/sys/swap.h
/include/sys/syscall.h
/include/sys/sysctl.h
/include/sys/sysinfo.h
/include/sys/syslog.h
/include/sys/sysmacros.h
/include/sys/time.h
/include/sys/times.h
/include/sys/timex.h
/include/sys/types.h
/include/sys/ucontext.h
/include/sys/uio.h
/include/sys/un.h
/include/sys/user.h
/include/sys/utsname.h
/include/sys/vfs.h
/include/sys/vt.h
/include/sys/wait.h
/include/syscall.h
/include/sysexits.h
/include/syslog.h
/include/tar.h
/include/termios.h
/include/tgmath.h
/include/time.h
/include/ucontext.h
/include/ulimit.h
/include/unistd.h
/include/utime.h
/include/utmp.h
/include/utmpx.h
/include/wchar.h
/include/wctype.h
/include/wordexp.h
/lib/crt1.o
/lib/crti.o
/lib/crtn.o
/lib/libcrypt.a
/lib/libdl.a
/lib/libm.a
/lib/libpthread.a
/lib/libresolv.a
/lib/librt.a
/lib/libutil.a
/lib/libxnet.a

%changelog
* Thu Apr 19 2012 Jeremy Huntwork <jhuntowrk@lightcubesolutions.com> - 0.8.9-1
- Initial version
