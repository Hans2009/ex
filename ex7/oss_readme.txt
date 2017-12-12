======================================================================
Intel Omni-Path Driver & Firmware Package

Package Version: 10.6.0.0.134
Component Versions:
  UEFI Driver: 1.6.0.0.0
  Config File: HFI_TYPE1_v1.0.1.0
  TMM:         10.4.0.0.146
  OS Driver:   0.9-294
======================================================================

(C) Copyright Lenovo 2017.
LIMITED AND RESTRICTED RIGHTS NOTICE: If data or software is delivered pursuant
a General Services Administration (GSA) contract, use, reproduction, or
disclosure is subject to restrictions set forth in Contract No. GS-35F-05925.

Note: Before using this information and the product it supports, please read
the general information in "Notices and Trademarks" in this document.


Intel 10.6 Omni-Path software/firmware can be obtained using the following links:

Intel Omni-Path Fabric Software (Including Intel Omni-Path Host Fabric Interface Driver)
Version: 10.6.0.0.134 (Latest) Date: 10/24/2017
https://downloadcenter.intel.com/download/27220

Intel Omni-Path Fabric Suite Fabric Manager GUI
Version: 10.6.0.0.136 (Latest) Date: 10/24/2017
https://downloadcenter.intel.com/download/27226

Intel Omni-Path Edge Switch Externally-Managed Firmware
Version: 10.6.0.0.117 (Latest) Date: 10/24/2017
https://downloadcenter.intel.com/download/27225

Intel Omni-Path Managed Switch Firmware
Version: 10.6.0.0.117 (Latest) Date: 10/24/2017
https://downloadcenter.intel.com/download/27224


CONTENTS
________

1.0  Overview
2.0  Installation and Setup Instructions
3.0  Unattended Mode
4.0  Web Information and Support Phone Number
5.0  Notices and Trademarks
6.0  Disclaimer


1.0  Overview
_____________

 This update contains device drivers and firmware for the Intel Omni-Path
 Host Fabric Adapter 100 Series 1 Port PCIe x8 and x16 adapters.

 1.1  Limitations

      This package is designed to perform fresh installations and upgrade
      installations only. It does not support preinstallation of the driver.
      This package only support TUI installation. No support for agentless
      installation is offerred.

 1.2  Problems Fixed

      See change history for details.

 1.3  Prerequisites

      Before installing any of the Omni-Path device drivers or firmware, the
      pre-requisite software RPMs MUST be installed. Boot to OS and install
      pre-requisites. Depending on the packages you choose, there may be
      additional prerequisites required. For additional information, refer to
      the Release Notes for your specific OS release and installation type.

 1.4  Dependencies

      The drivers in this package are meant to be used with the firmware and
      application software from the Intel 10.6 Omni-Path release. Using the
      drivers in this package with firmware and application software from any
      other Intel release may result in unexpected behavior.


2.0  Installation and Setup Instructions
________________________________________

 This package can only be updated with TUI commands.

 2.1  Installation Notes

      This driver revision supports the following operating systems:
        o Red Hat Enterprise Linux Server 7 Update 3
        o Red Hat Enterprise Linux Server 7 Update 4
        o SuSE Linux Enterprise Server 12 SP2
        o SuSE Linux Enterprise Server 12 SP3

       Note: A reboot is required following the installation of this driver
       package for the new drivers to be fully functional.

 2.2  Driver Installation Instructions

      2.2.1  Server Setup Prerequisite

        a. The 'Optimized Boot' setting may need to be disabled until the Omni-
           Path adapter is added to the exception list. This setting can be
           found in UEFI Setup under:

             Boot Manager -> Boot Options

        b. Ensure that Option ROM support is enabled for the slot where the
           Omni-Path adapter is installed. This setting can be found in UEFI
           Setup under:

             System Settings -> Devices and I/O Ports -> Enable/Disable Adapter
             Option ROM Support

      2.2.2  Operating System Prerequisite

        Boot to a supported operating system and ensure the following library
        packages are properly installed.

        SuSE Linux Enterprise Server 12
        -------------------------------

        The following packages are required for basic installation:
         o  libibmad5
         o  libibumad3
         o  libibumad-devel
         o  libibverbs1
         o  librdmacm1
         o  libibcm1
         o  ibacm
         o  qperf
         o  perftest
         o  rdma
         o  opensm-devel
         o  opensm-libs3
         o  libpsm_infinipath1
         o  libexpat1
         o  libelf-devel
         o  gcc-fortran
         o  libudev-devel
         o  texlive-latex
         o  texlive-babel-english
         o  texlive-psnfss
         o  texlive-courier
         o  bc
         o  rpm-build
         o  kernel-devel
         o  libstdc++-devel
         o  libipathverbs-rdmav2
         o  infiniband-diags
         o  rdma-core-devel

        The following packages are required to compile IFS software:
         o  libhfi1verbs-rdmav2
         o  libibverbs-devel
         o  librdmacm-devel
         o  ibacm-devel
         o  libopenssl-devel
         o  libuuid-devel
         o  libexpat-devel
         o  infinipath-psm-devel
         o  libibumad-devel
         o  valgrind-devel

        The following packages are required to rebuild all OFA source RPMs:
         o  readline-devel
         o  ncurses-devel
         o  libstdc++-devel
         o  glib2-devel
         o  kernel-syms
         o  libnuma-devel
         o  bison
         o  zlib-devel
         o  java


        Red Hat Enterprise Linux 7
        --------------------------

        The following packages are required for basic installation:
          o  libibmad
          o  libibumad
          o  libibumad-devel
          o  libibverbs
          o  librdmacm
          o  libibcm
          o  ibacm
          o  qperf
          o  perftest
          o  rdma
          o  infinipath-psm
          o  libhfi1
          o  expat
          o  elfutils-libelf-devel
          o  libstdc++-devel
          o  gcc-gfortran
          o  atlas
          o  c-ares
          o  tcl
          o  expect
          o  tcsh
          o  sysfsutils
          o  pciutils
          o  bc
          o  opensm-devel
          o  rpm-build
          o  redhat-rpm-config
          o  kernel-devel

        The following packages are required to compile IFS software:
          o  libibverbs-devel
          o  libibmad-devel
          o  librdmacm-devel
          o  ibacm-devel
          o  openssl-devel (1.0.1 or higher)
          o  libuuid-devel
          o  expat-devel
          o  infinipath-psm-devel
          o  valgrind-devel
          o  libpfm.x86 (RHEL* 7.3)
          o  opensm-libs
          o  papi.x86 (RHEL* 7.3)

        The following packages are required to rebuild all OFA source RPMs:
          o  readline-devel
          o  ncurses-devel
          o  opensm-devel
          o  glib2-devel
          o  numactl-devel
          o  libudev-devel
          o  java
          o  gcc-c++

      2.2.3  Install Software in Unattended Mode

        It is strongly suggested to install the necessary Omni-Path drivers in
        unattended mode. This will automatically ensure the correct software
        is fully installed. If manual/attended mode is desired, please skip to
        section 2.2.4 below.

          a. Extract the content of the IFS tgz file to a local directory.

          b. Execute the INSTALL script with the -a parameter and follow the on-
             screen prompts.

               ./INSTALL -a

          c. After installation is fully complete, reboot the server and skip to
             step 2.3 below.

      2.2.4  Install Software in Attended Mode

        If manual/attended installation mode is chosen, the default selections
        include libraries and utilities for connecting and managing an OPA
        fabric.

          a. Ensure the following are installed for the Omni-Path driver and
             firmware to load correctly:

               - Pre-Boot Components
               - OPA Stack
               - Intel HFI Components
               - OPA Tools
               - OFA OPA Development
               - OFA IP over OB

          b. Press 'P' once all selections have been made.

          c. Press Enter for each option and wait for installation to finish.

          d. On completion, press 'X' to properly exit the script.

          e. After installation is fully complete, reboot the server.

 2.3  Firmware Update Instructions

      2.3.1  Flash Omni-Path Adapter Firmware

        a. Navigate to the directory /usr/share/opa/bios_images/:

              cd /usr/share/opa/bios_images/

        b. Use the hfi1_eprom utility to flash the adapter firmware:

              hfi1_eprom -w -o HfiPcieGen3Loader_xxxx.rom -b HfiPcieGen3_xxxx.efi -c /lib/firmware/updates/hfi1_platform.dat

           Note: If multiple adapters are installed, specify each adapter to flash:

              hfi1_eprom -w -o HfiPcieGen3Loader_xxxx.rom -b HfiPcieGen3_xxxx.efi -c /lib/firmware/updates/hfi1_platform.dat -d /sys/bus/pci/devices/xxxx:xx:xx.x/resource0

        c. Verify the firmware was flashed correctly:

              hfi1_eprom -V -o
              hfi1_eprom -V -b
              hfi1_eprom -V -c

      2.3.2  Flash Thermal Management Microchip (TMM) Firmware

        a. Navigate to the directory /lib/firmware/updates/:

              cd /lib/firmware/updates/

        b. Use the opatmmtool utility to flash the adapter firmware:

              opatmmtool -f hfi1_smbus.fw fileversion
              opatmmtool -f hfi1_smbus.fw update

        c. Verify the TMM was flashed correctly:

              opahfirev

 2.4  Insallation Troubleshooting

      2.4.1  Verify Firmware Image Files

             The firmware image files should be located in the following
             locations:

             OPA UEFI Driver:        /opt/opa/bios_images/HfiPcieGen3*.efi
             OPA UEFI Driver Loader: /opt/opa/bios_images/HfiPcieGen3Loader*.rom
             OPA Configuration:      /lib/firmware/updates/hfi1_platform.dat
             OPA TMM Firmware:       /lib/firmware/updates/hfi1_smbus.fw

      2.4.2  Verify Application Software

             The commands `opainfo` and `opahfirev` should report adapter
             information and firmware/driver version details if all software
             is properly installed.

      2.4.3  Installation Logs

             If any errors are encountered during installation of the drivers
             or firmware, refer to the log file (/var/log/opa.log) for
             additional information.


3.0  Known Issues
__________________

 3.1  Unable to build kernel updates with SLES12 SP2 kISO

      If the SLES12 SP2 OS installation was completed using the Solid Driver
      Kit (or kISO tool), the following message may be displayed during the
      Omni-Path software installation (./INSTALL -a):

	   Unable to build ifs-kernel-updates-kmp-default: /lib/ modules/4.4.59-92.24.2.13249.1.PTF.1015452-default/build/scripts: not found
	   kernel-source or kernel-devel is required to build ifs-kernel-updates-kmp-default
	   ERROR - unable to perform builds due to need for additional OS rpms
	   Unable to Prepare OFA OPA Stack for Install
	   Failed to install all OPA software.

      To correct this, ensure the proper packages are installed:

        a. Uninstall the following RPMs (if installed):
             - kernel-source        (4.4.21_69 version)
             - kernel-syms          (4.4.21_69 version)
             - kernel-devel         (4.4.21_69 version)
             - kernel-default-devel (4.4.21_69 version)

        b. Install three RPMs from the SLES12 SP2 installation image (if not
           already installed):
             - pesign
             - pesign-obs-intergration
             - mozilla-nss-tools

        c. Install two RPMs from the Solid Driver Kit (or kISO) image:
             - kernel-source  (must be the 4.4.59-92 version to match kISO)
             - kernel-syms    (must be the 4.4.59-92 to match KIOS)

        d. Change to kernel build scripts directory (The installed Linux kernel
           will determine the exact directory path):

              cd /usr/src/linux-4.4.59-92.24.2.13249.1.PTF.1015452/scripts/

        e. Compile the unifdef script:

              gcc unifdef.c -o unifdef

        f. Run the Omni-Path software installer again (./INSTALL -a)


 3.2  Compatibility Issues with Red Hat Subscription Manager YUM Repository

      Issues have been seen when using Red Hat Subscription Manager's YUM
      repository. Newer RPMs from that repository have been found to obsolete
      RPMs required for Omni-Path. The following four (4) files include an
      update from RDMA to RDMA-CORE that will break Omni-Path installation:
          o  libibumad
          o  libibverbs
          o  libibcm
          o  librdmacm

      It is recommended to use the RHEL insallation DVD image for installation
      of compatible libraries.


 3.3  Rebuilding of All OFA Source RPMs May Fail

      Even when all required RPMs are installed, C++ compiler issues have been
      reported. This is typically encountered when the following installation
      options are selected:

         Install/Uninstall > Install All > Perform Selected Actions > Rebuild OFA SRPMs

      Intel is investigating this issue.


4.0  Web Information and Support Phone Number
_____________________________________________

 Please visit the following Intel website for additional drivers, management
 applications, or documentation:

 http://www.intel.com/content/www/us/en/high-performance-computing-fabrics/omni-path-architecture-fabric-overview.html


5.0  Notices and Trademarks
________________________________________

 Lenovo and the Lenovo logo are trademarks of Lenovo in the United States,
 other countries, or both.

 IBM is a registered trademark of International Business Machines Corporation
 in the United States and other countries.

 Windows is a trademark or registered trademark of Microsoft Corporation in the
 United States and other countries.

 Other company, product, and service names may be trademarks or service marks
 of others.


6.0  Disclaimer
_______________

 THIS DOCUMENT IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND.
 LENOVO DISCLAIMS ALL WARRANTIES, WHETHER EXPRESS OR IMPLIED,
 INCLUDING WITHOUT LIMITATION, THE IMPLIED WARRANTIES OF FITNESS
 FOR A PARTICULAR PURPOSE AND MERCHANTABILITY WITH RESPECT TO THE
 INFORMATION IN THIS DOCUMENT. BY FURNISHING THIS DOCUMENT, LENOVO
 GRANTS NO LICENSES TO ANY PATENTS OR COPYRIGHTS.

 Note to U.S. Government Users -- Documentation related to
 restricted rights -- Use, duplication or disclosure is subject
 to restrictions set forth in GSA ADP Schedule Contract with
 Lenovo Corporation.
