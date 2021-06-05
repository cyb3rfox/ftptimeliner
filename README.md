# FTP Timeliner

## Motivation

We currently work on a small case, where a custom made CMS gets breached regularly. That CMS is hosted on a shared server instance and the provider is reluctant to support the investigation. We want to have a timeline of the `wwwroot`. The only kind of access we have is FTP. So we need a small tool that recursively creates a timeline of the full `wwwroot` or any given directory. 

##Caveats

- The script needs `mlsd` command to work. That should not be a problem on most modern FTP servers.
- RFC3695 (https://datatracker.ietf.org/doc/html/draft-ietf-ftpext-mlst-16.txt) states the following:
  `Implementation Note: Implementors of this fact on UNIX(TM) systems should note that the unix "stat" "st_ctime" field does not give creation time, and that unix file systems do not record creation time at all.  Unix (and POSIX) implementations will normally not include this fact.`
  For that reason we are limited to the last modification timestamp. That will usually be enough though.

## Usage

`python ftptimeliner.py -s <server> -u <user> -p <password> -d / > ftp_timeline.csv`
