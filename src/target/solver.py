!pip install z3-solver

from z3 import *

se_domain=["mydaemon_t"]

my_object=[
    "mydaemon_var_run_t",
    "mydaemon_conf_t",
    "mydaemon_log_t"
    ]
sys_object=[
    "var_log_t",
    "var_run_t",
    "var_t",
    "etc_t",
    "node_t",
    "http_cache_port_t"
    ]

se_object= my_object + sys_object

se_target= se_domain + se_object

se_class=["dir","file","tcp_socket"]

se_perm=[
    "read","write","append","create","open","lock","search","getattr","add_name","bind","listen","setopt","name_bind","node_bind","unlink","remove_name"
    ]

allow={
    d:{
        t:{
            c:{
                p:Bool("allow {0} {1}:{2} {3}".format(d,t,c,p)) for p in se_perm
                } for c in se_class
            } for t in se_target
        } for d in se_domain
    }
print(allow)

type_transition={
    d:{
        t:{
            c:{
                o:Bool("type_transition {0} {1}:{2} {3}".format(d,t,c,o)) for o in se_object
                } for c in se_class
            } for t in se_target
        } for d in se_domain
}

all_vars= []
for d in se_domain:
    for t in se_target:
        for c in se_class:
            for p in se_perm:
                all_vars.append(allow[d][t][c][p])

for d in se_domain:
    for t in se_target:
        for c in se_class:
            for o in se_object:
                all_vars.append(type_transition[d][t][c][o])

s = Optimize()

cost = Sum([If(rule, 1, 0) for rule in all_vars])

s.minimize(cost)



constraints = [
    And(allow["mydaemon_t"]["var_log_t"]["dir"]["search"] == True),
    And(allow["mydaemon_t"]["var_log_t"]["dir"]["write"] == True),
    And(allow["mydaemon_t"]["var_log_t"]["dir"]["add_name"] == True),

    And(type_transition["mydaemon_t"]["var_log_t"]["file"]["mydaemon_log_t"] == True),
    And(allow["mydaemon_t"]["mydaemon_log_t"]["file"]["create"] == True),
    And(allow["mydaemon_t"]["mydaemon_log_t"]["file"]["open"] == True),
    And(allow["mydaemon_t"]["mydaemon_log_t"]["file"]["getattr"] == True),
    And(allow["mydaemon_t"]["mydaemon_log_t"]["file"]["append"] == True),




    And(allow["mydaemon_t"]["etc_t"]["dir"]["search"] == True),
    And(allow["mydaemon_t"]["etc_t"]["dir"]["getattr"] == True),

    And(allow["mydaemon_t"]["mydaemon_conf_t"]["file"]["open"] == True),
    And(allow["mydaemon_t"]["mydaemon_conf_t"]["file"]["getattr"] == True),
    And(allow["mydaemon_t"]["mydaemon_conf_t"]["file"]["read"] == True),




    And(allow["mydaemon_t"]["var_run_t"]["dir"]["search"] == True),
    And(allow["mydaemon_t"]["var_run_t"]["dir"]["write"] == True),
    And(allow["mydaemon_t"]["var_run_t"]["dir"]["add_name"] == True),
    And(allow["mydaemon_t"]["var_run_t"]["dir"]["remove_name"] == True),

    And(type_transition["mydaemon_t"]["var_run_t"]["file"]["mydaemon_var_run_t"] == True),
    And(allow["mydaemon_t"]["mydaemon_var_run_t"]["file"]["create"] == True),
    And(allow["mydaemon_t"]["mydaemon_var_run_t"]["file"]["open"] == True),
    And(allow["mydaemon_t"]["mydaemon_var_run_t"]["file"]["getattr"] == True),
    And(allow["mydaemon_t"]["mydaemon_var_run_t"]["file"]["write"] == True),
    And(allow["mydaemon_t"]["mydaemon_var_run_t"]["file"]["lock"] == True),
    And(allow["mydaemon_t"]["mydaemon_var_run_t"]["file"]["unlink"] == True),



    And(allow["mydaemon_t"]["var_t"]["dir"]["search"] == True),
    And(allow["mydaemon_t"]["var_t"]["dir"]["getattr"] == True),



    And(allow["mydaemon_t"]["mydaemon_t"]["tcp_socket"]["create"] == True),
    And(allow["mydaemon_t"]["mydaemon_t"]["tcp_socket"]["bind"] == True),
    And(allow["mydaemon_t"]["mydaemon_t"]["tcp_socket"]["listen"] == True),
    And(allow["mydaemon_t"]["mydaemon_t"]["tcp_socket"]["setopt"] == True),


    And(allow["mydaemon_t"]["http_cache_port_t"]["tcp_socket"]["name_bind"] == True),

    And(allow["mydaemon_t"]["node_t"]["tcp_socket"]["node_bind"] == True)
]


s.add(constraints)
print("制約の追加完了")


if s.check() == sat:

    m = s.model()

    print("policy_module(mydaemon, 1.0.0)")
    print("")



    print("require {")
    print("    type " + ", ".join(sys_object) + ";")

    print("    attribute logfile, pidfile, configfile;")

    print("    class file { ioctl read write create getattr setattr lock relabelfrom relabelto append map unlink link rename execute swapon quotaon mounton audit_access open execmod watch watch_mount watch_sb watch_with_perm watch_reads entrypoint };")
    print("    class dir { ioctl read write create getattr setattr lock relabelfrom relabelto append map unlink link rename execute swapon quotaon mounton audit_access open execmod watch watch_mount watch_sb watch_with_perm watch_reads add_name remove_name reparent search rmdir };")
    print("    class tcp_socket { create ioctl read write getattr setattr append bind connect listen accept getopt setopt shutdown recvfrom sendto name_bind node_bind name_connect };")
    print("    class filesystem { associate };")
    print("}")
    print("")

    print("########################################")
    print("#")
    print("# --- Declarations ---")
    print("#")
    print("")

    for t in se_domain:
        print("type {0};".format(t))
    for t in my_object:
        print("type {0};".format(t))

    print("")
    print("typeattribute mydaemon_log_t logfile;")
    print("typeattribute mydaemon_var_run_t pidfile;")
    print("typeattribute mydaemon_conf_t configfile;")
    print("")

    print("init_daemon_domain(mydaemon_t, mydaemon_exec_t)")
    print("")

    print("########################################")
    print("#")
    print("# --- Local Policy ---")
    print("#")

    print("")

    generated_associates = []

    for d in se_domain:
        for t in se_target:
            for c in se_class:
                for o in se_object:
                    if is_true(m.eval(type_transition[d][t][c][o])):
                        print("type_transition {0} {1}:{2} {3};".format(d,t,c,o))

                        if t == "var_run_t":
                            rule = "allow {0} tmpfs_t:filesystem associate;".format(o)
                            if rule not in generated_associates:
                                generated_associates.append(rule)

                        elif t == "var_log_t":
                            rule = "allow {0} fs_t:filesystem associate;".format(o)
                            if rule not in generated_associates:
                                generated_associates.append(rule)

    if generated_associates:
        print("")
        for rule in generated_associates:
            print(rule)
        print("")

    for d in se_domain:
        for t in se_target:
            for c in se_class:
                perms = []
                for p in se_perm:
                    if is_true(m.eval(allow[d][t][c][p])):
                        perms.append(p)
                if perms:
                    print("allow {0} {1}:{2} {{ {3} }};".format(d,t,c, " ".join(perms)))


else:
    print("Error")