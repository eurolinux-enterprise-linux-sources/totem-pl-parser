
#ifndef __totemplparser_marshal_MARSHAL_H__
#define __totemplparser_marshal_MARSHAL_H__

#include	<glib-object.h>

G_BEGIN_DECLS

/* VOID:STRING,STRING,STRING (./totemplparser-marshal.list:1) */
G_GNUC_INTERNAL void totemplparser_marshal_VOID__STRING_STRING_STRING (GClosure     *closure,
                                                                       GValue       *return_value,
                                                                       guint         n_param_values,
                                                                       const GValue *param_values,
                                                                       gpointer      invocation_hint,
                                                                       gpointer      marshal_data);

/* VOID:STRING,BOXED (./totemplparser-marshal.list:2) */
G_GNUC_INTERNAL void totemplparser_marshal_VOID__STRING_BOXED (GClosure     *closure,
                                                               GValue       *return_value,
                                                               guint         n_param_values,
                                                               const GValue *param_values,
                                                               gpointer      invocation_hint,
                                                               gpointer      marshal_data);

G_END_DECLS

#endif /* __totemplparser_marshal_MARSHAL_H__ */

