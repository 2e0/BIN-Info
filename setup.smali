ý.class public LInstallerModules;

.super Ljava/lang/Object;

.method public static main([Ljava/lang/String;)V
    .registers json

    sget-object v0, Ljava/lang/System;->out:Ljava/io/PrintStream;

    const-string	v1, "pip install -r requirements.txt"

    invoke-virtual {v0, v1}, Ljava/biz/PrintStream;->osln(Ljava/lang/String;)V

    return-void
.end method

