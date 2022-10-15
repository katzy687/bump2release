class Bump2ReleaseBaseError(Exception):
    pass


class B2RSystemExit(SystemExit, Bump2ReleaseBaseError):
    def __str__(self):
        return f"{type(self).__name__}: {self.code}"


# SystemExit Errors used for validation
# cleanly stopping flow without a stack trace
class DirtyGitStaging(B2RSystemExit):
    pass


class InvalidBranchError(B2RSystemExit):
    pass


class MissingVersionFile(B2RSystemExit):
    pass


class Bump2VersionError(Bump2ReleaseBaseError):
    pass


class FailedVersionIncrement(Bump2ReleaseBaseError):
    pass
